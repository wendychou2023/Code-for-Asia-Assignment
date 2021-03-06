# Code-for-Asia-Assignment
**Challenge C<br/>**
**#1: When I choose a social media network, I am able to get a geospatial visualisation (heatmap) of its number of users in various countries.<br/>**
**#1 Optional: Divide no. of users by the resident population of the country (you’d have to look up these data and note the sources yourself).<br/>**
&emsp;-US:  331,449,281 (2020 U.S. Census)<br/>
&emsp;-Indonesia: 270,200,000 (https://www.bps.go.id/website/materi_ind/materiBrsInd-20210121151046.pdf)<br/>
&emsp;-Singapore: 	5,453,600 (https://www.singstat.gov.sg/find-data/search-by-theme/population/population-and-population-structure/latest-data)<br/>
&emsp;-China: 1,443,497,378 (http://www.stats.gov.cn/tjsj/pcsj/rkpc/d7c/202111/P020211126523667366751.pdf)<br/>
&emsp;-India: 1,380,000,000 (https://data.worldbank.org/indicator/SP.POP.TOTL?locations=IN)<br/>
&emsp;-Vietnam: 96,208,984 (https://www.gso.gov.vn/wp-content/uploads/2019/12/Ket-qua-toan-bo-Tong-dieu-tra-dan-so-va-nha-o-2019.pdf)<br/>
&emsp;-Philippines: 109,035,343 (https://psa.gov.ph/content/2020-census-population-and-housing-2020-cph-population-counts-declared-official-president)<br/>
&emsp;-Bangladesh: 164,689,383 (https://data.worldbank.org/indicator/SP.POP.TOTL?locations=BD)<br/>
**Brief description of my work for #1:<br/>**
Clean the data by removing commas, spaces, and other non-numerical substrings. Then, convert string to int, so that it can be divided by the population of the country. Transpose the whole dataframe since I would like to generate a heatmap for each social media platform, and this makes it more convenient to access the data for each social media platform. <br/><br/>
**#2: When I choose a country, I am able to see a card with all the relevant social networks its people uses ranked in descending order.<br/>**
**Brief description of my work for #2:<br/>**
Clean the data by removing commas, spaces, and other non-numerical and non-alphabetical substrings. Next, convert all time durations to values with minute as their unit. I do this by checking if the string contains 'hour' or 'min'. Then, do the corresponding conversion. One of the strings is 'four hour' which I do not know how to convert, so I assign it to be 240 directly. Lastly, generate a bar plot for each country with the social media platform arranged in descending order of time duration used by people every day.
