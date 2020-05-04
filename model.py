import pandas as pd
import pickle
from sklearn.model_selection import RepeatedKFold

#---------------importing csv file-----------------
data_train=pd.read_csv('76+197train.csv', engine='python')
data_test=pd.read_csv('76+197test.csv')
#---------------creating copy of the file--------------
data_train1=data_train.copy()
data_test1=data_test.copy()

#-------------removing unwanted columns and rows-----------
data_train1.drop([217,218,219],axis=0, inplace=True)
data_train1=data_train1.dropna(axis=1)

new_train=data_train1
columns_list= list(data_train1.columns)

new_test=pd.get_dummies(data_test1, drop_first=True)
columns_list1= list(new_test.columns)

#------------separating input names from data--------
features=list(set(columns_list)-set(['label','pi','LENGTH','molecular weight','HYDROPHOBIC RESIDUE','BOMAN INDEX(kcal/mol)','AA','AC','AD','AE','AF','AG','AH','AI','AK','AL','AM','AN','AP','AQ','AR','AS','AT','AV','AW','AY','CA','CC','CD','CE','CF','CG','CH','CI','CK','CL','CM','CN','CP','CQ','CR','CS','CT','CV','CW','CY','DA','DC','DD','DE','DF','DG','DH','DI','DK','DL','DM','DN','DP','DQ','DR','DS','DT','DV','DW','DY','EA','EC','ED','EE','EF','EG','EH','EI','EK','EL','EM','EN','EP','EQ','ER','ES','ET','EV','EW','EY','FA','FC','FD','FE','FF','FG','FH','FI','FK','FL','FM','FN','FP','FQ','FR','FS','FT','FV','FW','FY','GA','GC','GD','GE','GF','GG','GH','GI','GK','GL','GM','GN','GP','GQ','GR','GS','GT','GV','GW','GY','HA','HC','HD','HE','HF','HG','HH','HI','HK','HL','HM','HN','HP','HQ','HR','HS','HT','HV','HW','HY','IA','IC','ID','IE','IF','IG','IH','II','IK','IL','IM','IN','IP','IQ','IR','IS','IT','IV','IW','IY','KA','KC','KD','KE','KF','KG','KH','KI','KK','KL','KM','KN','KP','KQ','KR','KS','KT','KV','KW','KY','LA','LC','LD','LE','LF','LG','LH','LI','LK','LL','LM','LN','LP','LQ','LR','LS','LT','LV','LW','LY','MA','MC','MD','ME','MF','MG','MH','MI','MK','ML','MM','MN','MP','MQ','MR','MS','MT','MV','MW','MY','NA','NC','ND','NE','NF','NG','NH','NI','NK','NL','NM','NN','NP','NQ','NR','NS','NT','NV','NW','NY','PA','PC','PD','PE','PF','PG','PH','PI','PK','PL','PM','PN','PP','PQ','PR','PS','PT','PV','PW','PY','QA','QC','QD','QE','QF','QG','QH','QI','QK','QL','QM','QN','QP','QQ','QR','QS','QT','QV','QW','QY','RA','RC','RD','RE','RF','RG','RH','RI','RK','RL','RM','RN','RP','RQ','RR','RS','RT','RV','RW','RY','SA','SC','SD','SE','SF','SG','SH','SI','SK','SL','SM','SN','SP','SQ','SR','SS','ST','SV','SW','SY','TA','TC','TD','TE','TF','TG','TH','TI','TK','TL','TM','TN','TP','TQ','TR','TS','TT','TV','TW','TY','VA','VC','VD','VE','VF','VG','VH','VI','VK','VL','VM','VN','VP','VQ','VR','VS','VT','VV','VW','VY','WA','WC','WD','WE','WF','WG','WH','WI','WK','WL','WM','WN','WP','WQ','WR','WS','WT','WV','WW','WY','YA','YC','YD','YE','YF','YG','YH','YI','YK','YL','YM','YN','YP','YQ','YR','YS','YT','YV','YW','YY','A.1','C.1','D.1','E.1','F.1','G.1','H.1','I.1','K.1','L.1','M.1','N.1','P.1','Q.1','R.1','S.1','T.1','V.1','W.1','Y.1','lam_1']))

features1=list(set(columns_list1)-set(['label','pi','LENGTH','molecular weight','HYDROPHOBIC RESIDUE','BOMAN INDEX(kcal/mol)','AA','AC','AD','AE','AF','AG','AH','AI','AK','AL','AM','AN','AP','AQ','AR','AS','AT','AV','AW','AY','CA','CC','CD','CE','CF','CG','CH','CI','CK','CL','CM','CN','CP','CQ','CR','CS','CT','CV','CW','CY','DA','DC','DD','DE','DF','DG','DH','DI','DK','DL','DM','DN','DP','DQ','DR','DS','DT','DV','DW','DY','EA','EC','ED','EE','EF','EG','EH','EI','EK','EL','EM','EN','EP','EQ','ER','ES','ET','EV','EW','EY','FA','FC','FD','FE','FF','FG','FH','FI','FK','FL','FM','FN','FP','FQ','FR','FS','FT','FV','FW','FY','GA','GC','GD','GE','GF','GG','GH','GI','GK','GL','GM','GN','GP','GQ','GR','GS','GT','GV','GW','GY','HA','HC','HD','HE','HF','HG','HH','HI','HK','HL','HM','HN','HP','HQ','HR','HS','HT','HV','HW','HY','IA','IC','ID','IE','IF','IG','IH','II','IK','IL','IM','IN','IP','IQ','IR','IS','IT','IV','IW','IY','KA','KC','KD','KE','KF','KG','KH','KI','KK','KL','KM','KN','KP','KQ','KR','KS','KT','KV','KW','KY','LA','LC','LD','LE','LF','LG','LH','LI','LK','LL','LM','LN','LP','LQ','LR','LS','LT','LV','LW','LY','MA','MC','MD','ME','MF','MG','MH','MI','MK','ML','MM','MN','MP','MQ','MR','MS','MT','MV','MW','MY','NA','NC','ND','NE','NF','NG','NH','NI','NK','NL','NM','NN','NP','NQ','NR','NS','NT','NV','NW','NY','PA','PC','PD','PE','PF','PG','PH','PI','PK','PL','PM','PN','PP','PQ','PR','PS','PT','PV','PW','PY','QA','QC','QD','QE','QF','QG','QH','QI','QK','QL','QM','QN','QP','QQ','QR','QS','QT','QV','QW','QY','RA','RC','RD','RE','RF','RG','RH','RI','RK','RL','RM','RN','RP','RQ','RR','RS','RT','RV','RW','RY','SA','SC','SD','SE','SF','SG','SH','SI','SK','SL','SM','SN','SP','SQ','SR','SS','ST','SV','SW','SY','TA','TC','TD','TE','TF','TG','TH','TI','TK','TL','TM','TN','TP','TQ','TR','TS','TT','TV','TW','TY','VA','VC','VD','VE','VF','VG','VH','VI','VK','VL','VM','VN','VP','VQ','VR','VS','VT','VV','VW','VY','WA','WC','WD','WE','WF','WG','WH','WI','WK','WL','WM','WN','WP','WQ','WR','WS','WT','WV','WW','WY','YA','YC','YD','YE','YF','YG','YH','YI','YK','YL','YM','YN','YP','YQ','YR','YS','YT','YV','YW','YY','A.1','C.1','D.1','E.1','F.1','G.1','H.1','I.1','K.1','L.1','M.1','N.1','P.1','Q.1','R.1','S.1','T.1','V.1','W.1','Y.1','lam_1']))
#------------storing the output values in y----------
y=new_train['label'].values
test_y=new_test['label'].values
#------------storing the input values in x-----------
x=new_train[features].values
test_x=new_test[features1].values

#---------cross validation--------
kf= RepeatedKFold(n_splits=5,n_repeats=150, random_state=10)

for train_index, test_index in kf.split(x):
   # print("train: ",train_index, "Validation: ", test_index)
    x_train, x_test =x[train_index], x[test_index]
    y_train, y_test =y[train_index], y[test_index]

#---------RF model-----------

#-----import model-----

from sklearn.ensemble import RandomForestClassifier

#create gaussian classifier
model=RandomForestClassifier(n_estimators=250, random_state=123)

#train model
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))



