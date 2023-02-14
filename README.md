# Mr Beast Analysis

### Folder Structure
- images : data visualization  
- video_api_data_full  
    - youtube api data pulled from the channel to get ids  
    - youtube api data pulled for each video  
- youtube_api_json_struct - structure of youtube api video and channels  
- youtube_api_pull_scripts - youtube api pulling and testing  
- full_video_analysis.ipynb - analysis on videos using YouTube api data  
- video_frame_change_analysis.ipynb - using python library to detect scene changes and measure them in number of frames  

# Problem Overview
Identify trends of Mr. Beast's Youtube Channel using the data provided by the Youtube API as well as the videos themselves.

# Analysis

All analysis can be found in ![this notebook](full_video_analysis.ipynb)

## Possible Trends To Investigate

Possible Trends to Investigate using Youtube API Data:
1. What factors contribute to view count, like count, comment count?
1. What is the optimal time to post?
1. How does title affect performance?
1. How do numbers in the title affect performance?
1. What is the optimal shot length?
1. What is the longest vs shortest shot a video should contain?


Other more open ended trends to investigate:
1. Do the 2 first visible lines of the description have impact? Do they even get viewed? (Desktop only)
1. Does the color which takes up the most percent of the thumbnail affect performance?
1. % of Jimmy in Title vs Performance
1. Why is having your mouth open in thumbnails so effective?
1. Performance vs If Jimmy is in Thumbnail?
1. Is money involved vs performance? Amount of money vs performance?

### Duration Vs View Count

The first investigation was if duration has an impact on views.

![alt text](/images/duration_vs_view_count.jpg)

There is some correlation between the length and performance. If we look at the above graph we can see in the most recent 100 videos longer than 4 minutes there is a slight correlation (0.281 Pearson Correlation) between the duration of a video and the view count of a video. That is not to say that more views is better, but if we look at that same set of videos, the highest view count of a video under 10 minutes was 172 million (World’s Most Dangerous Escape Room!). Ten videos over 10 minutes have gotten more views than this. Twelve videos were posted under 10 minutes, 88 videos being posted over 10 minutes. If we are striving for over 200 millions views on a video, which the staple videos of the channel have done (“$456,000 Squid Game In Real Life!”, “Last To Leave Circle Wins $500,000”, “I Spent 50 Hours In Solitary Confinement”), the shorter videos may need to change or videos under that length may need to be lengthened.

![alt text](/images/boxplot_view_times.jpg)


