from __future__ import print_function
import boto3
import json
import re

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "How would you like me to cook? Tell me power and duration."
    reprompt_text = "How would you like me to cook? Tell me power and duration."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def set_mode_in_session(intent, session):

    card_title = intent['name']
    session_attributes = {}
    client = boto3.client('iot-data', region_name='eu-west-1')

    if 'Power' in intent['slots'] and 'Duration' in intent['slots']:
        power = intent['slots']['Power']['value']
        isotime = intent['slots']['Duration']['value']

        #Format PT50M40S, PT1M3S, PT10M, PT1M, PT90S, PT5S, PT150S, etc
        minute = re.match(r'^PT[0-9]+M', isotime)
        if minute is None:
            minute = '0'
            speech_min = ''
        else:
            minute = minute.group(0).replace('M', '').replace('PT','')
            if minute == '1':
                speech_min = minute + " minute"
            else:
                speech_min = minute + " minutes"

        second = re.match(r'^PT.*[0-9]+S$', isotime)
        if second is None:
            second = '0'
            speech_sec = ""
        else:
            second = re.sub(r'^PT[0-9]*M', '', second.group(0)).replace('S', '').replace('PT', '')
            if second == '1':
                speech_sec = second + " second"
            else:
                speech_sec = second + " seconds"
            if speech_min != '':
                speech_sec = " and " + speech_sec

        speech_output = "Ok, cooking at " + power + " watts for " + speech_min + speech_sec
        power = int(power)
        minute = int(minute)
        second = int(second)

        response = client.publish(
            topic='microwave',
            qos=1,
            payload=json.dumps({
                "power": power,
                "min": minute,
                "sec": second
            } )
        )
        
        reprompt_text = ""
        should_end_session = True
    else:
        speech_output = "I'm not sure what you mean by that."
        reprompt_text = "I'm not sure what you mean by that."
        should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_full_setting_in_session(intent, session):

    card_title = intent['name']
    session_attributes = {}
    client = boto3.client('iot-data', region_name='eu-west-1')
    if 'Duration' in intent['slots']:
        duration = intent['slots']['Duration']['value']
        isotime = duration

            #Format PT50M90S
        duration = duration.replace('PT', '')
        duration = duration.replace('M', '')

        speech_output = "Ok, cooking at full power for" + duration + "minutes."

        response = client.publish(
            topic='microwave',
            qos=1,
            payload=json.dumps({
                "power": "full",
                "duration": isotime
            } )
        )

        reprompt_text = ""
        should_end_session = True
    else:
        speech_output = "I'm not sure what you mean by that."
        reprompt_text = "I'm not sure what you mean by that."
        should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MySettingIsIntent":
        return set_mode_in_session(intent, session)
    elif intent_name == "MySettingIsFullIntent":
        return get_full_setting_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
