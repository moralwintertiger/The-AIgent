# The AIgent v 0.1

## Using AI to connect writers & representation

<p align="center"><img src="https://raw.githubusercontent.com/moralwintertiger/flask-agent-v1/master/images/01_agent.png" width="700"></p>

### Challenge
Today, literary publishing is a <b>$20 billion industry</b>, with a serious bottleneck problem. Successful agents receive on the order of hundreds, if not thousands, of query letters daily. Before they can even sit down to the important task of reviewing a manuscript, hours of the day are devoted to scrolling through endless submission emails, and sorting the wheat from the chaff. 

### App Solution
The <a href="http://www.insilicoveritas.net:5000/">AIgent</a> is an app designed to solve this problem, by helping literary agents rapidly identify pitches that are a good match with their current portfolio. It leverages state-of-the-art techniques from ML and NLP to pinpoint the genre a pitch falls into, and automatically contextualizes it in terms of similar titles. In a centralized agency workflow, these techniques could be scaled to route submissions directly to agents that best match the query letter, saving agents (and writers!) time, money, and frustration.

### Repo Overview
* <a href="https://github.com/moralwintertiger/flask-agent-v1/tree/master/templates">App Design</a>
* <a href="https://github.com/moralwintertiger/flask-agent-v1/tree/master/data">Data Overview</a>
* <a href="https://github.com/moralwintertiger/flask-agent-v1/tree/master/similars_model">Technical Overview</a>

### Build Workflow
The AIgent was built in a 3-week period as part of an <a href="https://www.insightdatascience.com/">Insight Data Science</a> fellowship.<br><br>
* Scraped the metadata tags and synopses of >100k GoodReads titles using BeautifulSoup.<br>
* Leveraged pre-tained embeddings from the state-of-the-art BERT language model.<br>
* Built out a text classifier and transfer learning pipeline with TensorFlow, sklearn, and Pytorch.<br>
* Developed a robust classifier, achieving > 85% accuracy and > .9 F-scores, across 20 genres.<br>
* At inference, identified similar titles on the basis of embedding cosine similarity.<br>
* Deployed model as a Flask web app, hosted on AWS.<br>

<p align="center"><img src="https://raw.githubusercontent.com/moralwintertiger/flask-agent-v1/master/images/slide_02_workflow.png" width="600"></p>
