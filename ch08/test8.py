import numpy as np

# T,H = 5,4
# hs = np.random.randn(T,H)
# a = np.array([0.8,0.1,0.03,0.05,0.02])
#
# ar = a.reshape(5,1).repeat(4,axis=1)
# print(ar)
# #print(ar.shape)
# #(5,4)
#
#
# t = hs * ar
# print(t)
# #print(t.shape)
# #(5,4)
#
# c = np.sum(t,axis=0)
# print(c)
# #print(c.shape)

# N,T,H = 10,5,4
# hs = np.random.randn(N,T,H)
# a = np.random.randn(N,T)
# ar = a.reshape(N,T,1).repeat(H,axis=2)
# #ar = a.reshape(N,T,1) #ブロードキャストを使う場合
#
# t = hs * ar
# print(t.shape)
# #(10,5,4)
#
# c = np.sum(t,axis=1)
# print(c.shape)
# # (10,4)