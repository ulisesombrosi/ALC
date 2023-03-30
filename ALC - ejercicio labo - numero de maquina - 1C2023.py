#!/usr/bin/env python
# coding: utf-8

# ## Aritmética de punto flotante

# ¿Qué está pasando?

# In[ ]:


0.2 + 0.3


# In[ ]:


x = 0.3
print(x)


# In[ ]:


0.3 - 0.2


# - ¿Cuánto da $(\sqrt{2})^2 - 2$?
# 

# In[1]:


import numpy as np
np.sqrt(2)**2-2 


# - ¿Cuál es el límite cuando $n \rightarrow \infty$ de esta sucesión?
# $$
# \begin{aligned}
# x_1 &= \sqrt{2} \\
# x_{n+1} &= \frac{x_n \cdot x_n}{\sqrt{2}}
# \end{aligned}
# $$

# In[ ]:


x = np.sqrt(2)
print(x)
for i in range(100):
    x = (x * x) / np.sqrt(2)
print(x)


# ## Acumulación de errores

# 1. Se quiere calcular 
# $$
# \sum_{i=1}^{10^6} \frac{1}{i} \quad y \quad \sum_{i=1}^{2\cdot10^6} \frac{1}{i} 
# $$
# usando aritmética de simple precisión (float32).
# 
# Realizar para cada una de las expresiones un script que calcule el resultado. Qué se observa?

# In[15]:


import numpy as np

n = 7
s1 = np.float32(0)
for i in range(1,10**n+1):
    s1 += np.float32(1/i)

print("suma = ", s1)

s2 = np.float32(0)
for i in range(1,2*10**n+1):
    s2 += np.float32(1/i)

print("suma = ", s2)


# ¿Qué modificación harías para reducir los errores numéricos?

# In[19]:


import numpy as np

n = 6
s1 = np.float32(0)
for i in range(1,10**n+1):
    s1 += np.float32(1/i)

print("suma = ", s1)

s2 = s1
for i in range(10**n+1,2*10**n+1):
    s2 += np.float32(1/i)

print("suma = ", s2)



# 2. Utilizar las mismas estrategias para estimar $e$ mediante la serie
# $$
# e \approx \sum_{n=0}^{10} \frac{1}{n!}.
# $$
# 
# Comparar con el valor real.

# In[20]:


print(np.exp(1))

s = np.float32(0)
for n in range(0,11):
    s += 1/np.math.factorial(n)

print('suma =', s)


# 3. El siguiente código suma 1 10^8 veces. ¿Coincide la respuesta con el valor esperado? ¿Es posible modificar el código para calcular el valor correcto?

# In[25]:


print(float(10**8))

c = np.float64(0)

for i in range(10**8):
    c += np.float64(1)

print(c)


# In[ ]:




