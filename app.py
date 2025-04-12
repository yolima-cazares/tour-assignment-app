{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "568caeeb-d287-4c1e-83a5-1f25937b4766",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Título de la aplicación\n",
    "st.title(\"Aplicación Básica de Streamlit\")\n",
    "\n",
    "# Mostrar un texto simple\n",
    "st.write(\"¡Bienvenido a la aplicación de prueba de Streamlit!\")\n",
    "\n",
    "# Crear datos de ejemplo\n",
    "data = pd.DataFrame({\n",
    "    'Fecha': pd.date_range('20230101', periods=10),\n",
    "    'Valor': np.random.randn(10)\n",
    "})\n",
    "\n",
    "# Mostrar el DataFrame\n",
    "st.write(\"Datos generados aleatoriamente:\")\n",
    "st.dataframe(data)\n",
    "\n",
    "# Graficar los datos\n",
    "st.line_chart(data.set_index('Fecha'))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2024.02-py310",
   "language": "python",
   "name": "conda-env-anaconda-2024.02-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
