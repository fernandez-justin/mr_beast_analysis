
import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import csv

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

"""
snippet.tags[] -- A list of keyword tags associated with the video.
snippet.categoryId -- The YouTube video category associated with the video.
contentDetails.duration -- length, PT#M#S period of time 
"""

def get_ids():
    """
    VIDEO ID LOCATIONS:
    DONE-video_api_data_full\\video_id_pull_all_long.json
    video_api_data_full\\video_id_pull_medium_1_50.json
    video_api_data_full\\video_id_pull_medium_51_100.json
    video_api_data_full\\video_id_pull_medium_101_150.json
    """
    file = open('..\\video_api_data_full\\video_id_pull_medium_101_150.json')
    file_data = json.load(file)
    id_string_list = ''
    counter = 0
    for item in file_data['items']:
        #print(item['id']['videoId'])
        id_string_list += f"{item['id']['videoId']},"
        counter+=1
    #print(file_data['items'])
    #print(counter)
    #print(id_string_list)
    return id_string_list[:-1]
    

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1022140153515-fkhjjejep7fapb5clfnkibo39il7bbin.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # CHANGE, MAX RESULTS YT CAN RETURN IS 50
    ids_to_pull_data = get_ids()


    #fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics
    request = youtube.videos().list(
        fields = "items(id,snippet(title,publishedAt),contentDetails(duration),statistics)"
        , part= "snippet,contentDetails,statistics"
        , id=ids_to_pull_data
    )


    response = request.execute()

    json_object = json.dumps(response, indent=4)

    #print(response)

    # with open('..\\video_api_data_full\\full_videos_output_1_50.json','w') as f:
    #     f.write(json_object)
    # with open('..\\video_api_data_full\\full_videos_output_51_100.json','w') as f:
    #     f.write(json_object)
    with open('..\\video_api_data_full\\full_videos_output_101_150.json','w') as f:
        f.write(json_object)
    # with open('..\\video_api_data_full\\full_videos_output_all_long.json','w') as f:
    #     f.write(json_object)

if __name__ == "__main__":
    main()