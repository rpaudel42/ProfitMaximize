# TrueMotion Data Science Interview Project – Machine Learning

Welcome to TrueMotion, we are honestly glad you are here. I hope you're in for a special treat today.

Today you will engage on a project that will test your:

* Understanding of Machine Learning
* Command of programming
* Understanding of Feature Extraction
* Handling of Non standard data
* Solving an untypical problem that may seem confusing at first, and perhaps ambiguously posed
* Solving a problem under a time constraint

All of these technical skills are very important at TrueMotion on a day-to-day basis.

But most of all it's a chance for us to get to know you and for you to get to know us, and how we work at TrueMotion.

## Timeline

* **2-days-before**: Read over the project description, and discuss with Yuting or someone else your questions that arise.
* **1-day-before**: Explore the data, make visualizations, experiment with approaches. By this time you should have read the data in and have a concrete plan about how you are going to attack the problem. Again, reach out with questions, should any arise.
* **End-of-day**: Make sure to send your test set predictions over, and prepare to present to us the next morning.
* **Day-of**: You'll present to the team and have several one-on-one interviews. We'll go to lunch to take a break and enjoy a nice meal. And then you'll wrap up with one more interview and a discussion with HR.

## Project Description

The training data, `train.txt`, is a time series dataset, structured (purposefully) in a non-standard format.

The data contains 370 utterances of a vowel, by 9 male speakers; which correspond to labels 0-8. Note that every speaker speaks the exact same vowel. The data is divided into blocks, separated by `\n\n`. Each block contains a different number of rows, where each row corresponds to a point in time. Each block contains exactly 12 columns. To make the project easier since you only have a day to complete it, we transformed the origin audio signal into 12 [LPC Cepstrum coefficients](http://research.cs.tamu.edu/prism/lectures/sp/l9.pdf), which is a standard practice in speech recognition to achieve high performance.

In summary the training contains 370 blocks, at every point in time (rows) there exists a 12-dimensional vector (columns) corresponding to the LPC Cepstrum coefficients we calculated for you. Every block is actually one out of nine different speakers, speaking a vowel. All of the speakers in every instance are speaking the same vowel.

The rows of the blocks can vary anywhere from 7-29 points, which corresponds to 0.7s - 2.9 seconds.

Aditionally you will find, `test.txt`, which is the test dataset in the same format as `train.txt`.

You will also find another file, `train_block_labels.txt`, which lets you know which label corresponds to which block.

For example the first number in `train_block_labels.txt` is 31, which means that the first 31 blocks correspond to label 0. The second number in the file is 35, which means the second 35 blocks correspond to label 1.

## Deliverables

### Test Set Predictions
Email your predictions on the test set, and your code to Bill and Yuting (bill@gotruemotion.com, yuting@gotruemotion.com). Together we will evaluate your performance on the test set and go over your thought process and methodology for solving the problem.

Please submit your predictions on the test set in the following format:

```
block_num,prediction
0,3
1,2
2,3
3,5
4,0
...
268,8
269,1
```

That is make sure you have the headers:

1. `block_num`, which corresponds to the block on the test set,
2. `prediction`, which is a number `0-8`.

See `sample_submission.csv` for an example of the submission file.

### Training and Feature Extraction Code in Python

In addition to emailing over your predictions make sure you send over the python code you used to develop your predictions, commented just enough to understand what's going on

### Grading

The score we will grade the technical performance on, is the score of worst performing user. So make sure on your training set that all users are performing equally well. But this makes up a relatively small part of the overall project.

## Advice

The time is going to pass by faster than you think. I would reccommend you to:

* First get a feedback loop going. Just try some simple naive features, and a scoring metric so that as you iterate you can know which changes have a positive effect and which don't. Innovation is proportional to the number of iterations you can complete.
* Plot the data to gain an intuition
* Make sure you are not overfitting
* Don't overly stress yourself. We realize a single day is not a lot of time to complete everything exactly to your liking, maybe you'll get lucky or unlucky. What really matters in that you are thinking through the problem in a principled, logical way.
