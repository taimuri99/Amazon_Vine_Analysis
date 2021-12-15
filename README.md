# Amazon_Vine_Analysis
Module 16 PySpark, AWS &amp; SQL: Big Data
## Overview of the analysis of the Vine program

The aim of this challenge was to analyse Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review. Many datasets were analysed to determine if there is any bias toward favorable reviews from Vine members in your dataset.

## Results

The dataset chosen for this challenge were reviews on sport products. The data was inputted into a dataframe and then specific columns were chosen to make the vine_df dataframe as shown below:

<img width="606" alt="Screenshot 2021-12-15 at 00 43 50" src="https://user-images.githubusercontent.com/87828174/146130180-c57c1c8a-a7a4-4655-af27-e0f6307a6f91.png">

The data is filtered into a new dataframe to show only those entries where the total_votes count is equal to or greater than 20 to pick reviews that are more likely to be helpful and to avoid having division by zero errors later on. This dataframe was further filtered to create a new DataFrame of selected rows where the number of helpful_votes divided by total_votes was equal to or greater than 50%. From this dataframe two seperate tables were created:

#### Review was written as part of the Vine program.

<img width="603" alt="Screenshot 2021-12-15 at 00 50 36" src="https://user-images.githubusercontent.com/87828174/146130859-7eac90a2-2487-4c0f-8565-9aa8366da0cc.png">

#### Review was not part of the Vine program.

<img width="600" alt="Screenshot 2021-12-15 at 00 51 16" src="https://user-images.githubusercontent.com/87828174/146130927-57b47951-5bc4-4c7e-a175-6d5c1fd0dd64.png">

Using these dataframes we were able to analyse the share of 5 star reviews for both types of reviewers. This is seen in the next section.

### How many Vine reviews and non-Vine reviews were there?
#### Vine Reviews

<img width="262" alt="Screenshot 2021-12-15 at 00 54 11" src="https://user-images.githubusercontent.com/87828174/146131237-e762b236-98fd-450d-8094-ad33f9acdb96.png">

There are **334** Vine reviews.

#### Non Vine Reviews

<img width="273" alt="Screenshot 2021-12-15 at 00 55 38" src="https://user-images.githubusercontent.com/87828174/146131359-54f5367b-feea-44ec-bca2-98a6eefeb0de.png">

There are **61614** Non Vine reviews.

### How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?
#### 5 Star Vine Reviews

<img width="474" alt="Screenshot 2021-12-15 at 00 56 41" src="https://user-images.githubusercontent.com/87828174/146131481-61dc33b6-c574-430b-9b49-adc713d9f5d9.png">

There are **139** 5 Star Vine reviews.

#### 5 Star Non Vine Reviews

<img width="491" alt="Screenshot 2021-12-15 at 00 57 39" src="https://user-images.githubusercontent.com/87828174/146131599-cf24c5bb-678e-4fa2-9065-70556812984d.png">

There are **32665** 5 Star Non Vine reviews.

### What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?
#### Percentage of 5 Star Vine Reviews

<img width="457" alt="Screenshot 2021-12-15 at 00 59 14" src="https://user-images.githubusercontent.com/87828174/146131775-1b7f2c9c-443d-4bc1-a047-6d85f358a33b.png">

**42%** of the Vine reviews were 5 Star reviews.

#### Percentage of 5 Star Non Vine Reviews

<img width="506" alt="Screenshot 2021-12-15 at 01 00 27" src="https://user-images.githubusercontent.com/87828174/146131895-32c87995-8883-4117-8341-a49cd9493c62.png">

**53%** of the Non Vine reviews were 5 Star reviews.

## Summary

<img width="387" alt="Screenshot 2021-12-15 at 01 01 07" src="https://user-images.githubusercontent.com/87828174/146131995-e9af0f22-06ce-4b65-aeab-57391b7b6f0f.png">

Looking at this result we see that 42% of the Vine reviews were 5 star reviews while 53% of the non Vine reviews were 5 star reviews. Since Vine reviews had a less percentage of 5 star reviews, there is no evidence of positivity bias for reviews in the Vine program for this dataset.

An additional analysis of the other datasets may show different information and yield different results. Therefore after performing a similar analysis for each data set one can see then on average if Vine reviews yield evidence for positivity bias.

An additional analysis for this dataset can be to plot the mean, median and mode to see where the average review lies for Vine and Non Vine for this dataset.




