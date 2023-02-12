# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1022140153515-fkhjjejep7fapb5clfnkibo39il7bbin.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        #fields="items(id(videoId),snippet(title,publishedAt))",
        part="snippet",
        channelId='UCX6OQ3DkcsbYNE6H8uQQuVA',
        order='date',
        type='video',
        videoDuration='medium',
        maxResults=50
    )
    response = request.execute()

    json_object = json.dumps(response, indent=4)

    #print(response)

    # with open('..\\video_api_data_full\\full_videos_output_1_50.txt','w') as f:
    #     f.write(json_object)
    with open('..\\video_api_data_full\\video_id_pull_1_50.json','w') as f:
        f.write(json_object)

if __name__ == "__main__":
    main()