//状態空間表現から伝達関数を得る
A=[0 1;-2 -3]; b=[0;1]; c=[1 2]; d=0;
ss_sys=syslin('c',A,b,c,d);
tf_sys=ss2tf(ss_sys)

