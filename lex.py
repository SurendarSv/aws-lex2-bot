{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "id": "78ce5f46",
      "metadata": {
        "id": "78ce5f46",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5e1fa684-0ed4-4f16-8857-b11833eabbab"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting boto3\n",
            "  Downloading boto3-1.26.148-py3-none-any.whl (135 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m135.6/135.6 kB\u001b[0m \u001b[31m12.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting botocore<1.30.0,>=1.29.148 (from boto3)\n",
            "  Downloading botocore-1.29.148-py3-none-any.whl (10.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.8/10.8 MB\u001b[0m \u001b[31m67.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting jmespath<2.0.0,>=0.7.1 (from boto3)\n",
            "  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)\n",
            "Collecting s3transfer<0.7.0,>=0.6.0 (from boto3)\n",
            "  Downloading s3transfer-0.6.1-py3-none-any.whl (79 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.8/79.8 kB\u001b[0m \u001b[31m10.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.10/dist-packages (from botocore<1.30.0,>=1.29.148->boto3) (2.8.2)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.25.4 in /usr/local/lib/python3.10/dist-packages (from botocore<1.30.0,>=1.29.148->boto3) (1.26.15)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.30.0,>=1.29.148->boto3) (1.16.0)\n",
            "Installing collected packages: jmespath, botocore, s3transfer, boto3\n",
            "Successfully installed boto3-1.26.148 botocore-1.29.148 jmespath-1.0.1 s3transfer-0.6.1\n"
          ]
        }
      ],
      "source": [
        "!pip install boto3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "id": "27e24502",
      "metadata": {
        "id": "27e24502"
      },
      "outputs": [],
      "source": [
        "import boto3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "161a7d07",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "161a7d07",
        "outputId": "6ef012a4-1511-4abe-ab03-02be287cc1fe"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<botocore.client.LexRuntimeV2 at 0x7f7b97829a10>"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "\n",
        "client = boto3.client('lexv2-runtime',region_name='us-east-1',aws_access_key_id='AKIAYLRXNOXIGEOWYR2V',aws_secret_access_key='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')\n",
        "client"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Book hotel\n",
        "# Mumbai\n",
        "# 25-08-2022\n",
        "# king"
      ],
      "metadata": {
        "id": "_R_5u-jkvgXE"
      },
      "id": "_R_5u-jkvgXE",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\n",
        "\n",
        "botId = "1DRIAMQFFX"\n",
        "botAliasId = "YWGTHNBKWN"\n",
        "localeId = "en_US"\n",
        "sessionId = "100"
      ],
      "metadata": {
        "id": "UjQFiTJ4bilv"
      },
      "id": "UjQFiTJ4bilv",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2361010a",
      "metadata": {
        "id": "2361010a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "18428e90-0806-4238-f3f5-1e1844e772af"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'ResponseMetadata': {'RequestId': 'afca95a0-b457-472b-aadf-97b237ba73ea',\n",
              "  'HTTPStatusCode': 200,\n",
              "  'HTTPHeaders': {'x-amzn-requestid': 'afca95a0-b457-472b-aadf-97b237ba73ea',\n",
              "   'strict-transport-security': 'max-age=31536000; includeSubDomains',\n",
              "   'x-content-type-options': 'nosniff',\n",
              "   'date': 'Tue, 23 Aug 2022 18:24:51 GMT',\n",
              "   'content-type': 'application/json',\n",
              "   'content-length': '655'},\n",
              "  'RetryAttempts': 0},\n",
              " 'messages': [{'content': 'What city will you be staying in?',\n",
              "   'contentType': 'PlainText'}],\n",
              " 'sessionState': {'dialogAction': {'type': 'ElicitSlot',\n",
              "   'slotToElicit': 'Location'},\n",
              "  'intent': {'name': 'BookHotel',\n",
              "   'slots': {'CheckInDate': None,\n",
              "    'Location': None,\n",
              "    'Nights': None,\n",
              "    'RoomType': None},\n",
              "   'state': 'InProgress',\n",
              "   'confirmationState': 'None'},\n",
              "  'originatingRequestId': 'afca95a0-b457-472b-aadf-97b237ba73ea'},\n",
              " 'interpretations': [{'nluConfidence': {'score': 0.95},\n",
              "   'intent': {'name': 'BookHotel',\n",
              "    'slots': {'CheckInDate': None,\n",
              "     'Location': None,\n",
              "     'Nights': None,\n",
              "     'RoomType': None},\n",
              "    'state': 'InProgress',\n",
              "    'confirmationState': 'None'}},\n",
              "  {'intent': {'name': 'FallbackIntent', 'slots': {}}}],\n",
              " 'sessionId': '100'}"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='Book hotel')\n",
        "response"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Intent:\",response['sessionState']['intent']['name'])\n",
        "print(\"Next Action:\",response['sessionState']['dialogAction']['type'])\n",
        "print(\"Next Slot:\",response['sessionState']['dialogAction']['slotToElicit'])\n",
        "print(\"Prompt or Msg:\",response['messages'][0]['content'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z1Mt2gKrdNKM",
        "outputId": "628ee285-4661-4ef0-c0d3-a3bfc538d9a0"
      },
      "id": "z1Mt2gKrdNKM",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intent: BookHotel\n",
            "Next Action: ElicitSlot\n",
            "Next Slot: Location\n",
            "Prompt or Msg: What city will you be staying in?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f563c36f",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f563c36f",
        "outputId": "a978ed9b-1f44-4f4c-da46-210e98b76181"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intent: BookHotel\n",
            "Next Action: ElicitSlot\n",
            "Next Slot: CheckInDate\n",
            "Prompt or Msg: What day do you want to check in?\n"
          ]
        }
      ],
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='Mumbai')\n",
        "print(\"Intent:\",response['sessionState']['intent']['name'])\n",
        "print(\"Next Action:\",response['sessionState']['dialogAction']['type'])\n",
        "print(\"Next Slot:\",response['sessionState']['dialogAction']['slotToElicit'])\n",
        "print(\"Prompt or Msg:\",response['messages'][0]['content'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ab59a1d4",
      "metadata": {
        "id": "ab59a1d4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2aeb37c4-f25b-4207-899f-d6143a90e43b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intent: BookHotel\n",
            "Next Action: ElicitSlot\n",
            "Next Slot: Nights\n",
            "Prompt or Msg: How many nights will you be staying?\n"
          ]
        }
      ],
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='25-08-2022')\n",
        "print(\"Intent:\",response['sessionState']['intent']['name'])\n",
        "print(\"Next Action:\",response['sessionState']['dialogAction']['type'])\n",
        "print(\"Next Slot:\",response['sessionState']['dialogAction']['slotToElicit'])\n",
        "print(\"Prompt or Msg:\",response['messages'][0]['content'])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='3')\n",
        "print(\"Intent:\",response['sessionState']['intent']['name'])\n",
        "print(\"Next Action:\",response['sessionState']['dialogAction']['type'])\n",
        "print(\"Next Slot:\",response['sessionState']['dialogAction']['slotToElicit'])\n",
        "print(\"Prompt or Msg:\",response['messages'][0]['content'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jhPZ-sHNZAV3",
        "outputId": "0d62ffb2-dcc4-49c1-e181-376a88f11049"
      },
      "id": "jhPZ-sHNZAV3",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intent: BookHotel\n",
            "Next Action: ElicitSlot\n",
            "Next Slot: RoomType\n",
            "Prompt or Msg: What type of room would you like, queen, king, or deluxe?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='king')\n",
        "response"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A5k35hFFc99i",
        "outputId": "305cebe2-73cc-4eac-874d-0088c5e9b1fe"
      },
      "id": "A5k35hFFc99i",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'ResponseMetadata': {'RequestId': '8e284e11-ac4f-46bd-9286-e7140c4c250f',\n",
              "  'HTTPStatusCode': 200,\n",
              "  'HTTPHeaders': {'x-amzn-requestid': '8e284e11-ac4f-46bd-9286-e7140c4c250f',\n",
              "   'strict-transport-security': 'max-age=31536000; includeSubDomains',\n",
              "   'x-content-type-options': 'nosniff',\n",
              "   'date': 'Tue, 23 Aug 2022 18:28:10 GMT',\n",
              "   'content-type': 'application/json',\n",
              "   'content-length': '1385'},\n",
              "  'RetryAttempts': 0},\n",
              " 'messages': [{'content': 'Okay, I have you down for a 3 night stay in Mumbai starting 2022-08-25. Shall I book the reservation?',\n",
              "   'contentType': 'PlainText'}],\n",
              " 'sessionState': {'dialogAction': {'type': 'ConfirmIntent'},\n",
              "  'intent': {'name': 'BookHotel',\n",
              "   'slots': {'CheckInDate': {'value': {'originalValue': '25-08-2022',\n",
              "      'interpretedValue': '2022-08-25',\n",
              "      'resolvedValues': ['2022-08-25']}},\n",
              "    'Location': {'value': {'originalValue': 'Mumbai',\n",
              "      'interpretedValue': 'Mumbai',\n",
              "      'resolvedValues': ['mumbai']}},\n",
              "    'Nights': {'value': {'originalValue': '3',\n",
              "      'interpretedValue': '3',\n",
              "      'resolvedValues': ['3']}},\n",
              "    'RoomType': {'value': {'originalValue': 'king',\n",
              "      'interpretedValue': 'king',\n",
              "      'resolvedValues': ['king']}}},\n",
              "   'state': 'InProgress',\n",
              "   'confirmationState': 'None'},\n",
              "  'originatingRequestId': 'afca95a0-b457-472b-aadf-97b237ba73ea'},\n",
              " 'interpretations': [{'nluConfidence': {'score': 1.0},\n",
              "   'intent': {'name': 'BookHotel',\n",
              "    'slots': {'CheckInDate': {'value': {'originalValue': '25-08-2022',\n",
              "       'interpretedValue': '2022-08-25',\n",
              "       'resolvedValues': ['2022-08-25']}},\n",
              "     'Location': {'value': {'originalValue': 'Mumbai',\n",
              "       'interpretedValue': 'Mumbai',\n",
              "       'resolvedValues': ['mumbai']}},\n",
              "     'Nights': {'value': {'originalValue': '3',\n",
              "       'interpretedValue': '3',\n",
              "       'resolvedValues': ['3']}},\n",
              "     'RoomType': {'value': {'originalValue': 'king',\n",
              "       'interpretedValue': 'king',\n",
              "       'resolvedValues': ['king']}}},\n",
              "    'state': 'InProgress',\n",
              "    'confirmationState': 'None'}},\n",
              "  {'intent': {'name': 'FallbackIntent', 'slots': {}}}],\n",
              " 'sessionId': '100'}"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = client.recognize_text(\n",
        "    botId=botId,\n",
        "    botAliasId=botAliasId,\n",
        "    localeId=localeId,\n",
        "    sessionId=sessionId,\n",
        "    text='Yes')\n",
        "response"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMR9E_-mdAr6",
        "outputId": "9f2d6408-06a3-4ce4-ba09-e920d2568d83"
      },
      "id": "SMR9E_-mdAr6",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'ResponseMetadata': {'RequestId': 'e4d4b731-50f3-4b3f-a0b0-7ae76340ccbd',\n",
              "  'HTTPStatusCode': 200,\n",
              "  'HTTPHeaders': {'x-amzn-requestid': 'e4d4b731-50f3-4b3f-a0b0-7ae76340ccbd',\n",
              "   'strict-transport-security': 'max-age=31536000; includeSubDomains',\n",
              "   'x-content-type-options': 'nosniff',\n",
              "   'date': 'Tue, 23 Aug 2022 18:29:04 GMT',\n",
              "   'content-type': 'application/json',\n",
              "   'content-length': '1322'},\n",
              "  'RetryAttempts': 0},\n",
              " 'messages': [{'content': 'Thanks, I have placed your reservation',\n",
              "   'contentType': 'PlainText'}],\n",
              " 'sessionState': {'dialogAction': {'type': 'Close'},\n",
              "  'intent': {'name': 'BookHotel',\n",
              "   'slots': {'CheckInDate': {'value': {'originalValue': '25-08-2022',\n",
              "      'interpretedValue': '2022-08-25',\n",
              "      'resolvedValues': ['2022-08-25']}},\n",
              "    'Location': {'value': {'originalValue': 'Mumbai',\n",
              "      'interpretedValue': 'Mumbai',\n",
              "      'resolvedValues': ['mumbai']}},\n",
              "    'Nights': {'value': {'originalValue': '3',\n",
              "      'interpretedValue': '3',\n",
              "      'resolvedValues': ['3']}},\n",
              "    'RoomType': {'value': {'originalValue': 'king',\n",
              "      'interpretedValue': 'king',\n",
              "      'resolvedValues': ['king']}}},\n",
              "   'state': 'Fulfilled',\n",
              "   'confirmationState': 'Confirmed'},\n",
              "  'originatingRequestId': 'afca95a0-b457-472b-aadf-97b237ba73ea'},\n",
              " 'interpretations': [{'nluConfidence': {'score': 1.0},\n",
              "   'intent': {'name': 'BookHotel',\n",
              "    'slots': {'CheckInDate': {'value': {'originalValue': '25-08-2022',\n",
              "       'interpretedValue': '2022-08-25',\n",
              "       'resolvedValues': ['2022-08-25']}},\n",
              "     'Location': {'value': {'originalValue': 'Mumbai',\n",
              "       'interpretedValue': 'Mumbai',\n",
              "       'resolvedValues': ['mumbai']}},\n",
              "     'Nights': {'value': {'originalValue': '3',\n",
              "       'interpretedValue': '3',\n",
              "       'resolvedValues': ['3']}},\n",
              "     'RoomType': {'value': {'originalValue': 'king',\n",
              "       'interpretedValue': 'king',\n",
              "       'resolvedValues': ['king']}}},\n",
              "    'state': 'Fulfilled',\n",
              "    'confirmationState': 'Confirmed'}},\n",
              "  {'intent': {'name': 'FallbackIntent', 'slots': {}}}],\n",
              " 'sessionId': '100'}"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "867aMkbgdHNQ"
      },
      "id": "867aMkbgdHNQ",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.7"
    },
    "colab": {
      "name": "AWS Lex boto3 : Youtube.ipynb",
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}