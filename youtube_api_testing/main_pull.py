
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

    with open('..\\all_100_video_ids.csv', newline='') as csvfile:
        csvReader = csv.reader(csvfile)

        id_string_list_1_50 = ''
        id_string_list_51_100 = ''

        for id_list in csvReader:
            for id in id_list[:50]:
                id_string_list_1_50 = str(f"{id_string_list_1_50},{id}")
            for id in id_list[51:]:
                id_string_list_51_100 = str(f"{id_string_list_51_100},{id}")
        
        id_string_list_1_50 = id_string_list_1_50[1:] # cutting initial
        id_string_list_51_100 = id_string_list_51_100[1:] # cutting initial
    
    # id_string_list_1_50 = id_string_list[:50]
    # id_string_list_51_100 = id_string_list[51:]

    #fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics
    request = youtube.videos().list(
        fields = "items(id,snippet(title,publishedAt),contentDetails(duration),statistics)"
        , part= "snippet,contentDetails,statistics"
        , id=id_string_list_51_100
    )


    response = request.execute()

    json_object = json.dumps(response, indent=4)

    #print(response)

    # with open('..\\video_api_data_full\\full_videous_output_1_50.txt','a') as f:
    #     f.write(json_object)
    with open('..\\video_api_data_full\\full_videous_output_51_100.txt','a') as f:
        f.write(json_object)

if __name__ == "__main__":
    main()