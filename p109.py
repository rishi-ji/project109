import pandas as pd
import statistics as st
import csv

df = pd.read_csv('p109.csv')
reading_score_list=df['readingScore'].tolist()
reading_score_m=st.mean(reading_score_list)
reading_score_n=st.median(reading_score_list)
reading_score_q=st.mode(reading_score_list)
reading_score_s=st.stdev(reading_score_list)

print(reading_score_m)
print(reading_score_n)
print(reading_score_q)
print(reading_score_s)



reading_score_first_start,reading_score_first_end=reading_score_m-reading_score_s,reading_score_m+reading_score_s
reading_score_sec_start,reading_score_sec_end=reading_score_m-(2*reading_score_s),reading_score_m+(2*reading_score_s)
reading_score_third_start,reading_score_third_end=reading_score_m-(3*reading_score_s),reading_score_m+(3*reading_score_s)

reading_score_list_first_std_data=[result for result in reading_score_list if result>reading_score_first_start and result<reading_score_first_end]
reading_score_list_sec_std_data=[result for result in reading_score_list if result>reading_score_sec_start and result<reading_score_sec_end]
reading_score_list_third_std_data=[result for result in reading_score_list if result>reading_score_third_start and result<reading_score_third_end]

print("{}% of data for reading_score lies within first standard diviation".format(len(reading_score_list_first_std_data)*100.0/len(reading_score_list)))
print("{}% of data for reading_score lies within second standard diviation".format(len(reading_score_list_sec_std_data)*100.0/len(reading_score_list)))
print("{}% of data for reading_score lies within third standard diviation".format(len(reading_score_list_third_std_data)*100.0/len(reading_score_list)))