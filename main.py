import praw
from datetime import datetime

# list of keywords that the bot searches the submissions for
# enter your keywords into the list
KEYWORDS = ['python', 'programming', 'help']

# Text that the reddit bot replies with to selected submissions
REPLY_TEXT = ''

def main(myClient_id, myClient_secret, myUsername, myPassword, mySubreddit):
    # praw reddit instance - logging in to reddit account
    # get client_id and client_secret form Reddit API app creator
    # username and password is your reddit user credentials
    reddit = praw.Reddit(client_id = myClient_id ,
                        client_secret = myClient_secret,
                        username = myUsername,
                        password = myPassword,
                        user_agent = 'Default Reddit bot (by/ u/user)')

    # (optinal) check if logging into your account is successfull
    print(reddit.user.me())

    # choosing your subreddit - "All" for choosing the whole Reddit site
    subreddit = reddit.subreddit(mySubreddit)

    # iterate through submissions in subreddit
    for submission in subreddit.stream.submissions():
        process_submission(submission)

# function for processing the submissions
def process_submission(submission):
    # convert submission title to lowercase
    title_to_lowercase = submission.title.lower()
    # iterate through your keywords
    for keyword in KEYWORDS:
        # check if a keyword is in a submission title
        if keyword in title_to_lowercase:
            # print info about submission
            unix_time = submission.created_utc
            utc_time = datetime.utcfromtimestamp(unix_time).strftime('%d-%m-%y %H:%M:%S')
            print(f'Submission title: {submission.title}')
            print(f'Submission created date: {utc_time}')
            print(f'Submission link: {submission.url}')
            print(30 * '-')
            # (optinal) make the bot reply to the submissions
            try: 
                submission.reply(REPLY_TEXT)
                print('The bot replied to the submission')
            except Exception as e:
                print(e)
            # break so the bot dosen't react twice or more to the same submission
            break

if __name__ == '__main__':
    main()