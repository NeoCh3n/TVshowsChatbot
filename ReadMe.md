#This is a Cloud Computing Group Program.

It is a more practical chatbot.

Context:
your basic requirement is to *create a ChatBot that uses Google Gemini API*, while 10% points (2 points) will consider the application context and the output quality of your ChatBot.

During the Covid lock down people are keeping social distance with their friends.We want to develop a chatbot to help them learn/perform watching TV shows on streaming platforms (Netflix/Disney+/Bilibili etc.), at the same time, to help them connect with other people.

####Key point Here: Watch TV shows; Connect with people.

Depends on the number of members in your group, you are going to prototype 1 to 2 features on your chatbot. 
A feature can be, but not limited to, one of the followings:
 • Reading/writing a TV show review

Note: the data of the chatbot does not need to be accurate or comprehensive, but your chatbot should be able to accept natural language as input.

####Technical Requirement

Your project should fulfill the following requirements. Fail to comply will incur penalty:
 • the app must have a database system (SQL or redis or any other) from a database cloud provider other than RedisLab (e.g. Firebase, Heroku PostgreSQL).
 • the app must be hosted on a cloud platform other than Heroku;
 • the app must use the ChatGPT API (Google);
 • the app must be managed by git;
 • container technologies must be used;
 
Additional marks will be given to groups who are able to demonstrate:
 • Good Practices of DevOps workflow;
 • the Scalability of their app;
 • the Load balancing of their app;
 • the Orchestration of multiple containers;
 • *Security measurements of their app*;
 • or any practical consideration

Meanwhile user interface/project completeness/coding quality/documentation will carry only a very small fraction of marks. Most of the marks will be given based on the innovation of your app and the ability of demonstration of cloud technology competence.
## Use our Docker image

You can use the following command to pull and run our Docker image:

```bash
docker pull ghcr.io/tokiharashori/neoch3n/tvshowschatbot:tvshowschatbotv2
docker run -it ghcr.io/tokiharashori/neoch3n/tvshowschatbot:tvshowschatbotv2

Last updated: 2024-03-29
