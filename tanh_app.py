import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function", layout="wide")
st.title("Hyperbolic Tangent (Tanh) Activation Function")
st.write("Tanh maps input values to an output between -1 and 1.")
st.latex(r"f(x) = \\tanh(x)")

st.sidebar.header("Input Controls")
x = st.sidebar.slider("Choose an input value (x)", -10.0, 10.0, 2.0, 0.1)
y = np.tanh(x)

c1, c2 = st.columns(2)
c1.metric("Input (x)", f"{x:.2f}")
c2.metric("Tanh Output", f"{y:.4f}")

st.subheader("Tanh Function Graph")
xgrid = np.linspace(-10, 10, 400)
ygrid = np.tanh(xgrid)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(xgrid, ygrid, label="Tanh", linewidth=2)
ax.scatter([x], [y], s=80, label="Selected input/output")
ax.axhline(0, linewidth=0.8)
ax.axhline(1, linewidth=0.8, linestyle="--")
ax.axhline(-1, linewidth=0.8, linestyle="--")
ax.axvline(0, linewidth=0.8)
ax.set(xlabel="Input (x)", ylabel="Output f(x)", title="Tanh Activation Function")
ax.set_ylim(-1.1, 1.1)
ax.grid(True)
ax.legend()
st.pyplot(fig)
plt.close(fig)

st.subheader("Interpretation")
st.write(f"For an input of {x:.2f}, Tanh produces an output of {y:.4f}.")
if x < 0:
    st.write("A negative input produces a negative output.")
elif x > 0:
    st.write("A positive input produces a positive output.")
else:
    st.write("When the input is 0, the Tanh output is also 0.")
st.info("Tanh is zero-centred and produces both negative and positive output values.")
