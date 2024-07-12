{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "be13cccc-b8c2-4645-8540-17229e8052b5",
   "metadata": {},
   "source": [
    "# Importing Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "861ffe7b-2a6f-4b3f-aada-ff9e78213e9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0c84e38-4a04-4363-97c0-ef57aab41a0e",
   "metadata": {},
   "source": [
    "### Read Data from SQL Database"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "76119504-a4be-4f61-a755-5156088d739d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2541571c-fac2-46b2-8422-d4a031f9c061",
   "metadata": {},
   "outputs": [],
   "source": [
    "con = sqlite3.connect(r'C:\\Users\\vinay\\Projects\\P-1_Password_Strength/password_data.sqlite')  # connecting with sqlite DB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3763b388-458f-45f7-b29b-bd4769fafb6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_sql_query(\"SELECT  * FROM Users\", con)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6fdf8699-fb7a-4f00-939f-bb164a81e9b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>password</th>\n",
       "      <th>strength</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>zxe870819</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>xw46454nr23l</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>soporte13</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>accounts6000webhost.com</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>c443balg</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index                 password  strength\n",
       "0      0                zxe870819         1\n",
       "1      1             xw46454nr23l         1\n",
       "2      2                soporte13         1\n",
       "3      3  accounts6000webhost.com         2\n",
       "4      4                 c443balg         1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4f82312-f2f6-455e-9eec-912eba23e1e3",
   "metadata": {},
   "source": [
    "## Data Cleaning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "81c9b156-30f8-4ae7-91e8-03625ef941bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['index', 'password', 'strength'], dtype='object')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ece824f0-62e1-4dee-9b74-07dff56dbc76",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop(['index'], axis=1, inplace=True)    #removing unwanted columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "294268de-aede-42c5-94f0-3a6d53bceb2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "99995    False\n",
       "99996    False\n",
       "99997    False\n",
       "99998    False\n",
       "99999    False\n",
       "Length: 100000, dtype: bool"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.duplicated()   #checking for duplicatesdata.duplicated()   #checking for duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d5cf4b00-88f9-4dac-ab3f-7826d6ceb15f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "password    False\n",
       "strength    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().any()          # checking for missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4bee2ba7-2548-45f9-ac50-a6b087845fd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "password    object\n",
       "strength     int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes    # checking data types of columns data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b7657303-f853-4a28-a1ca-978c8ef1a7de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 0], dtype=int64)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"strength\"].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "471344fb-d3b2-4507-883f-7f4b341a69ed",
   "metadata": {},
   "source": [
    "## Performing Semantic Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "26661897-b70f-4414-8c9c-dd67b70b4f4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "99995    False\n",
       "99996    False\n",
       "99997    False\n",
       "99998    False\n",
       "99999    False\n",
       "Name: password, Length: 100000, dtype: bool"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"password\"].str.isnumeric()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "77a42c2c-0e94-47f1-9bb4-dcd175b51c61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(26, 2)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.isnumeric()].shape   # no.of people having password consists of numbers only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d0dd9179-2f9b-49d0-9c13-e08f2255353a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50, 2)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.isalpha()].shape   # no.of people having password consists of alphabets letters only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8ca3d46d-72d1-49d8-abb1-5c17a0cb47d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1506, 2)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.isupper()].shape   # no.of people having password consists of uppercase letters only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9ba75165-e05d-421d-885e-8232ff529662",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(86678, 2)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.islower()].shape   # no.of people having password consists of lowercase letters only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5abe304a-27de-497c-8ed0-8953841c6702",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(97203, 2)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.isalnum()].shape   # no.of people having password consists of alphanuymeric letters only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "67ad670c-be70-4e29-8606-7dcc74756c8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(932, 2)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].str.istitle()].shape   # no.of people having password consists of starting letter as capital "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e8c57ca1-97a7-4923-aa1a-1740542df9d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'!\"#$%&\\'()*+,-./:;<=>?@[\\\\]^_`{|}~'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import string\n",
    "string.punctuation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2ab8c5fb-323e-44a9-a0a0-d4abdc9678f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_semantics(row):\n",
    "    for char in row:\n",
    "        if char in string.punctuation:\n",
    "            return 1\n",
    "        else:\n",
    "            pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "79ad0a75-1371-4ba7-9fec-3b157e4dbf24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        NaN\n",
       "1        NaN\n",
       "2        NaN\n",
       "3        1.0\n",
       "4        NaN\n",
       "        ... \n",
       "99995    NaN\n",
       "99996    NaN\n",
       "99997    NaN\n",
       "99998    NaN\n",
       "99999    NaN\n",
       "Name: password, Length: 100000, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"password\"].apply(find_semantics)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "934db3a6-cb71-4442-9c1d-99923200b55f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>password</th>\n",
       "      <th>strength</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>accounts6000webhost.com</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>12463773800+</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>p.r.c.d.g.</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>cita-cita</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>180</th>\n",
       "      <td>karolina.susnina0U</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99748</th>\n",
       "      <td>maiselis.com</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99845</th>\n",
       "      <td>hosting4meze!@#</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99954</th>\n",
       "      <td>semista_bakung15</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99980</th>\n",
       "      <td>halflife2010!LEB</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99988</th>\n",
       "      <td>lbhtrnjh@</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2663 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                      password  strength\n",
       "3      accounts6000webhost.com         2\n",
       "68                12463773800+         1\n",
       "98                  p.r.c.d.g.         1\n",
       "145                  cita-cita         1\n",
       "180         karolina.susnina0U         2\n",
       "...                        ...       ...\n",
       "99748             maiselis.com         1\n",
       "99845          hosting4meze!@#         2\n",
       "99954         semista_bakung15         2\n",
       "99980         halflife2010!LEB         2\n",
       "99988                lbhtrnjh@         1\n",
       "\n",
       "[2663 rows x 2 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"password\"].apply(find_semantics)==1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4c7ce062-82c7-4427-b6fe-63f8483d8548",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>password</th>\n",
       "      <th>strength</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>zxe870819</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>xw46454nr23l</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>soporte13</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>accounts6000webhost.com</td>\n",
       "      <td>2</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>c443balg</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99995</th>\n",
       "      <td>obejofi215</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99996</th>\n",
       "      <td>fmiopvxb64</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99997</th>\n",
       "      <td>czvrbun38</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99998</th>\n",
       "      <td>mymyxe430</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99999</th>\n",
       "      <td>glqjhkxb467</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100000 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                      password  strength  length\n",
       "0                    zxe870819         1       9\n",
       "1                 xw46454nr23l         1      12\n",
       "2                    soporte13         1       9\n",
       "3      accounts6000webhost.com         2      23\n",
       "4                     c443balg         1       8\n",
       "...                        ...       ...     ...\n",
       "99995               obejofi215         1      10\n",
       "99996               fmiopvxb64         1      10\n",
       "99997                czvrbun38         1       9\n",
       "99998                mymyxe430         1       9\n",
       "99999              glqjhkxb467         1      11\n",
       "\n",
       "[100000 rows x 3 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"length\"] = data[\"password\"].str.len()\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0ed0a13e-b2d3-4c91-a492-05070a524825",
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq_lowercase(row):\n",
    "    return len([char for char in row if char.islower()])/len(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "4cada268-4c35-4c66-99bf-61d121e1c1b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq_uppercase(row):\n",
    "    return len([char for char in row if char.isupper()])/len(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b06e340e-113e-4464-9679-63900a2f0c95",
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq_numeric(row):\n",
    "    return len([char for char in row if char.isdigit()])/len(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e5dd1457-3b53-4072-9041-2a92644b46bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"lowercase_freq\"] = np.round(data[\"password\"].apply(freq_lowercase), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "106d15d9-ac61-4a04-befb-b250e44750ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"uppercase_freq\"] = np.round(data[\"password\"].apply(freq_uppercase), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9d127bf8-ffbe-4c55-b14a-be3e9f078e8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"digit_freq\"] = np.round(data[\"password\"].apply(freq_numeric), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f6689108-a958-4e58-b138-be2e6747d352",
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq_special_char(row):\n",
    "    for char in row:\n",
    "        special_chars=[]\n",
    "        if not char.isalpha() and not char.isdigit():\n",
    "            special_chars.append(char)\n",
    "    return len(special_chars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3cf6e8f6-e414-4263-aa94-36af3e7921bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"special_char_freq\"] = np.round(data[\"password\"].apply(freq_special_char), 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "7bbdcd54-6a41-462a-8384-1486973e83fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>password</th>\n",
       "      <th>strength</th>\n",
       "      <th>length</th>\n",
       "      <th>lowercase_freq</th>\n",
       "      <th>uppercase_freq</th>\n",
       "      <th>digit_freq</th>\n",
       "      <th>special_char_freq</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>zxe870819</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "      <td>0.33</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.67</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>xw46454nr23l</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "      <td>0.42</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.58</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>soporte13</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "      <td>0.78</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.22</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       password  strength  length  lowercase_freq  uppercase_freq  digit_freq  \\\n",
       "0     zxe870819         1       9            0.33             0.0        0.67   \n",
       "1  xw46454nr23l         1      12            0.42             0.0        0.58   \n",
       "2     soporte13         1       9            0.78             0.0        0.22   \n",
       "\n",
       "   special_char_freq  \n",
       "0                0.0  \n",
       "1                0.0  \n",
       "2                0.0  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"special_char_freq\"] = data[\"special_char_freq\"]/data[\"length\"]\n",
    "data.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7e34ee2-733a-4c9c-96c3-10b6b8ed6ec2",
   "metadata": {},
   "source": [
    "## Performing Descriptive Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ca12f560-24cd-429f-8239-2925a2042d54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['password', 'strength', 'length', 'lowercase_freq', 'uppercase_freq',\n",
       "       'digit_freq', 'special_char_freq'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "37e67b53-768a-4eb1-91ae-036cdc91cef2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"4\" halign=\"left\">length</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>min</th>\n",
       "      <th>max</th>\n",
       "      <th>mean</th>\n",
       "      <th>median</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>strength</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>6.550947</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8</td>\n",
       "      <td>13</td>\n",
       "      <td>9.611074</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14</td>\n",
       "      <td>220</td>\n",
       "      <td>15.953421</td>\n",
       "      <td>16.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         length                       \n",
       "            min  max       mean median\n",
       "strength                              \n",
       "0             1    7   6.550947    7.0\n",
       "1             8   13   9.611074    9.0\n",
       "2            14  220  15.953421   16.0"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[['length','strength']].groupby(['strength']).agg([\"min\",\"max\",\"mean\",\"median\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "85043023-5c2e-44d0-8754-3a220e2edecf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         length                       \n",
      "            min  max       mean median\n",
      "strength                              \n",
      "0             1    7   6.550947    7.0\n",
      "1             8   13   9.611074    9.0\n",
      "2            14  220  15.953421   16.0\n",
      "\n",
      "\n",
      "         lowercase_freq                       \n",
      "                    min   max      mean median\n",
      "strength                                      \n",
      "0                   0.0  1.00  0.707861   0.71\n",
      "1                   0.0  0.92  0.630550   0.67\n",
      "2                   0.0  0.92  0.425160   0.40\n",
      "\n",
      "\n",
      "         uppercase_freq                       \n",
      "                    min   max      mean median\n",
      "strength                                      \n",
      "0                   0.0  1.00  0.012858   0.00\n",
      "1                   0.0  0.92  0.007917   0.00\n",
      "2                   0.0  0.89  0.367897   0.43\n",
      "\n",
      "\n",
      "         digit_freq                       \n",
      "                min   max      mean median\n",
      "strength                                  \n",
      "0               0.0  1.00  0.275598   0.29\n",
      "1               0.0  0.92  0.359650   0.33\n",
      "2               0.0  0.89  0.192597   0.19\n",
      "\n",
      "\n",
      "         special_char_freq                           \n",
      "                       min       max      mean median\n",
      "strength                                             \n",
      "0                      0.0  0.333333  0.001361    0.0\n",
      "1                      0.0  0.125000  0.000546    0.0\n",
      "2                      0.0  0.071429  0.002120    0.0\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "cols = ['length', 'lowercase_freq', 'uppercase_freq',\n",
    "       'digit_freq', 'special_char_freq']\n",
    "for columns in cols:\n",
    "    print(data[[columns, 'strength']].groupby(['strength']).agg([\"min\", \"max\", \"mean\", \"median\"]))\n",
    "    print('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "05030495-d7c0-45e9-943b-6d36ea9bb14f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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d9ezZ0+n9gPMkp2drR07dujTTz/Vjh072AELAACglMjMzNTy5cv14osvavny5crMzDQ7JDjIaUW4KlWqaO3atXnaP/3002vuXgX3YLFY3HqkIlCSkpOTndoPMMP69et15513qmfPnho6dKh69uypO++8U+vXrzc7NAAAAFyHyZMnq379+powYYJWr16tCRMmqH79+po8ebLZoZnOE2obTlsTbsKECerXr5+2bNliWxPuu+++04YNG8rkFuV9+/bVX3/95VY3wPjx4/Xpp59q3759ZocCuK2zZ886tR9Q0tavX6+BAwfK19fXrj0lJUUDBw7UkiVLFBUVZVJ0AAAAKK7Jkydr8eLFedqzs7Nt7c7eBJHahnM5bSRc3759tX37dlWuXFmffPKJPv74Y1WqVEnbtm1T3759nXWZUufSpUtmh+BSa9asUVhYmO2xZs0as0MCiuyxxx4zOwTAIdnZ2RozZowMw1C7du302Wef6ddff9Vnn32mdu3ayTAM/etf/2JqKgCn6Nevn12e169fP7NDAoBSKzMzU0uXLi2wz9KlS02bmlraaxvO4tRtMW6//XatWbNGP/zwg/bu3as1a9bo9ttvd+Yl3M5HH32kpk2byt/fX1WqVNFdd92l559/XqtXr9Znn30mi8Uii8WiLVu26OjRo7JYLPrggw/UqVMn+fn56e2335YkrVy5Uo0aNZKfn58aNmyohQsX2q6Re9wnn3yizp07KyAgQM2aNdOOHTvsYlm2bJltu+EHH3xQs2fPVuXKlSVJq1at0oQJE/Tjjz/aYlq1apXt2JSUFD344IMKCAhQvXr19Pnnn1/39yYsLEyjR4+2axs9enSRFkQFzBYQEKCNGzeyjTc8wo4dO3Tq1CnddttteuONN9SiRQuVL19eLVq00BtvvKFWrVopJSUlz+8PACiqsLAwbdq0ya5t06ZN5HkA4CKrVq1STk5OgX1ycnLs/s4vCmobJcOpRbjDhw/rxRdfVK9evXTixAlJ0oYNG3TgwAFnXsZtJCcn67HHHtNTTz2lgwcPasuWLXrooYf08ssvq2fPnurWrZuSk5OVnJystm3b2o574YUXNGzYMB08eFBdu3bVsmXLNHbsWE2ePFkHDx7Uq6++qnHjxmn16tV21xs7dqxGjhypffv2qX79+nrssceUlZUlSdq2bZsGDRqkZ599Vvv27dPdd99tNyf80Ucf1XPPPafGjRvbYnr00Udtr0+YMEE9e/bU/v371b17dz3++ONKTU0t9vfm6gSsbt26Bb4OuKuLFy8qNTVVFy9eNDsUoFC5Ccxzzz2XZ/t5Ly8vPffcc3b9AKA4CsvjyPMAwPm+++4729fe3t4aMmSIvvnmGw0ZMkTe3t759nMUtY2S47Q14WJjYxUVFaV27dpp69atmjRpkoKDg7V//34tX75cH330kbMu5TaSk5OVlZWlhx56SHXq1JEkNW3aVJLk7++vjIwMVa9ePc9xw4cP10MPPWR7PnHiRM2aNcvWFh4erl9++UVLlixRnz59bP1Gjhype+65R9LlG6tx48aKi4tTw4YNNX/+fEVFRWnkyJGSpPr162v79u364osvbPFUqFBB5cqVyzemvn372qbcvfrqq5o/f7527dqV7463hblyyukDDzygzz77TEePHrV7ntvv8ccfL/L5AcCdpaWlKS4uzpRr534AFh8fn+9W6keOHLH1++mnn0o0tlwRERHy9/c35doArp+jU0779eunFStWuDgaACg7/vzzT0mXP1g9cOCA9u3bp3379qljx4569tln1aBBAxmGYetXFNQ2So7TinCjR4/WpEmTFB0drcDAQFt7586d9dprrznrMm6lWbNm6tKli5o2baquXbsqMjJSjzzyiG644YYCj2vVqpXt65MnTyoxMVH9+vXTgAEDbO1ZWVmqVKmS3XG33HKL7esaNWpIuvyHVMOGDXXo0CE9+OCDdv1bt25tu1ELc+W5y5cvr8DAQNsfc0V15RTU3IJbfs9Hjx5NEQ5AqRMXF6fu3bubGsOYMWMKfP29997Te++9V0LR2Fu3bp0tqQPgea6egnq9/QAAjjlz5oykyzuAdurUya7YVrNmTVksFhmGYetXFNQ2So7TinA//fST3nnnnTzt1apV06lTp5x1GbditVoVExOj7du3a9OmTZo/f77Gjh2rnTt3Fnhc+fLlbV/nzuletmxZnvXzrFar3fMrh5haLBa74w3DsLXlMgzD4fdy5blzz1/YfPOiqF69uo4dO+a08wGu0qBBAx06dMihfkB+IiIitG7dOlOunZ2drSeeeEJnzpxR69at1a5dO82ZM0cjRozQtm3btGvXLlWuXFlvvfVWnt8xJSUiIsKU6wIAAHiy3L/Zs7Oz84x2u/L51X/bO4LaRslxWhGucuXKSk5OVnh4uF373r17FRoa6qzLuB2LxaJ27dqpXbt2eumll1SnTh2tXbtWPj4+Du0+FxISotDQUB05cuS6RoU1bNhQu3btsmvbvXu33XNHY3Km+fPnq0ePHrbnn376qYYOHVqiMQBF8ddffzm1H8oef39/U0d6zZgxQ08//bT2799v+70wZ84c2xTQ6dOn69ZbbzUtPgClR+PGjfXII4/o6NGjqlu3rj766KNSuxY0AJitTZs2io+Pd6hfcVDbKBlOK8L16tVLL7zwgj788ENbpXHbtm0aOXKkevfu7azLuJWdO3fqq6++UmRkpIKDg7Vz506dPHlSjRo1Unp6ujZu3KhDhw6pSpUqeYZfXmn8+PEaNmyYKlasqKioKGVkZGj37t06ffq0oqOjHYpl6NCh6tChg2bPnq377rtPX3/9tdavX29XQa5bt67i4+O1b98+1apVS4GBgfL19b3u70NB/Pz8CnwOuBtHhyq705Bm4EpRUVFaunSpXnnlFf3xxx+29qpVq2rcuHGKiooyMToApcmBAwcougFACenWrVu+sw/z61dU1DZKjtN2R508ebJq166t0NBQnT9/XjfffLM6dOigtm3b6sUXX3TWZdxKxYoVtXXrVnXv3l3169fXiy++qFmzZikqKkoDBgxQgwYN1KpVK1WrVk3btm275nn69++v5cuXa9WqVWratKk6duyoVatW5RlVWJB27dpp8eLFmj17tpo1a6YNGzZoxIgRdkWvhx9+WN26dVPnzp1VrVo1vfvuu9f1/h0xYMAAhYWF6Y477lBYWJjd3HDAHTk61LkoQ6KBkhYVFaVvv/1WU6dOlSRNnTpV33zzDQU4AAAAD3X16LDr7Xclahslx2I44S9JwzCUkJCgatWq6dixY/rhhx+Uk5Oj5s2bq169es6I06XOnj2rSpUq6cyZM3l2k0tPT1d8fLzCw8M9bhTXgAED9Ouvv+qbb75x6nkL+54UZVv6xMREZ4YGXDfuX5QmP/30k7p3785mCC5SUP4A98G/k3PxexKejPsXnmzo0KH69NNPC+3Xo0cPzZ8/P087tY28CvqeuCp/cMp0VMMwVK9ePR04cED16tXTjTfe6IzToohmzpypu+++W+XLl9f69eu1evVqLVy4sMTjGD9+vMaPHy/pcoX6448/tr125fPcPgAAAAAA4NquXGakcuXKatiwoe35r7/+aluz+sp+nspdahuu4JTpqF5eXqpXr16p3QXVU+zatUt33323mjZtqsWLF2vevHnq379/icfRr18/29e5BbcqVarYPb+6H+DOche0BwCgrOvTp49T+wEAHHPl5gTNmzfXvffeq4cfflj33nuvmjdvnm8/T+UutQ1XcNrGDNOnT9fzzz+vRYsWqUmTJs46LYrggw8+MDsEm8TERLvh3lcXaBneDU+SlpZmdggAALiFunXrOrUfAKDoNm/erM2bN5sdhsu4U23D2ZxWhHviiSd08eJFNWvWTD4+PnlGjqSmpjrrUvAQiYmJWrFihd200/HjxzMCDgAAwEP17t1bkyZN0g033KDMzEydPXvW9lrFihXl4+Oj06dPq3fv3iZGCXeWlpamuLg4s8Mo1E8//WTKdSMiIpiFgXx5eXkpJyfHoX5wX04rws2dO9dZp0Ip0q9fP4puAAB4sOjoaIf7zp4924WRwB34+PhowIABWrx4sapWraqpU6fqrrvu0pdffqmZM2cqJSVFgwYNko+Pj9mhwk3FxcWpe/fuZodRKLNiZDMlXMs///lPvf766w71g/u6riJcdHS0Jk6cqPLlyys8PFxt27ZVuXJOq+sBAADAZHv37tUPP/ygrKwsNWjQQJL022+/yWq1qkWLFrZ+FovFrBBRwsaOHStJWrZsmUaPHm1rt1qtGjRokO11ID8RERFat26dKdcuSmHNrBgjIiJMuS7cX8uWLZ3aD+a4rorZ/Pnz9cILL6h8+fLq3LmzkpOTFRwc7KzYUAo899xzdvO5e/bsqVmzZpkYEQAAKIr77rtPgYGBWr16tW644QZJ0unTp/Xkk0+qffv2eu6550yOEGYYO3as7r//ft1zzz0yDEMWi0X//ve/GcGDQvn7+5t2n1y9bnVB/QB34+ho89mzZ+vuu+92cTQorusqwtWtW1fz5s1TZGSkDMPQjh07bMnZ1Tp06HA9l4IHyu8X3AcffKAPPviAX2wAAHiIWbNmadOmTXY53g033KBJkyYpMjKSIlwZdXWeZxiGbZQReR7cWWGFOO5fuKvff//dqf1gjusqws2YMUODBg3SlClTZLFY9OCDD+bbz2KxKDs7+3ou5TGSkpJKdBOKoKAghYaGltj1HHX1LzaLxSLDMOxe5xccAADu7+zZszp+/LgaN25s137ixAmdO3fOpKhgpivzPF9fXw0dOlTz589XRkaG7XXyPLizaxXiuG/hzhz9neus383UNlzjuopwPXr0UI8ePXT+/HlVrFhRhw4dKtPTUZOSktS5c2elpaWV2DX9/f21efNmt7pZr/xEfOTIkXr22Wdtz1977TXNnDnT1o+pqQAAuLcHH3xQTz75pGbNmqU77rhDkvTdd9/p+eef10MPPWRydChphw4dsn29c+dO1axZU5L07LPP6s8//9Ttt99u65e7hiDgjhITE/XTTz+pe/fubIYAXIXahus4ZReFChUqaPPmzQoPDy90Y4apU6dq0KBBqly5sjMu7VZSU1OVlpamiaOeU7gDaw1cr/jERI2bPkupqalFvlEXLlyoGTNmKDk5WY0bN9bcuXPVvn17p8R15Rpwx44ds/uU6YknnrDrRxEOAAD3tnjxYo0cOVJPPPGELl26JEkqV66c+vXrpxkzZpgcHUpa165dJV0eAZdbcLuSj4+PMjMz1bVrVx09erSEowMAOAO1Dddx2lamHTt2dKjfq6++qp49e5bKIlyu8LAwNarnvrvavP/++xo+fLgWLlyodu3aacmSJYqKitIvv/yi2rVrO/Vab7/9doHPAQCAewsICLAluIcPH5ZhGIqIiFD58uXNDg0myF1iJnfq6dUyMzPt+gEAPBe1DefzKukLXrkuGMwxe/Zs9evXT/3791ejRo00d+5chYWFadGiRS67ZmEjJAEAgHtLTk5WcnKy6tevr/Lly5PTlVFWq9Wp/QAAKC4zahvXq8SLcDBXZmam9uzZo8jISLv2yMhIbd++3SnXuHL4aNu2bZWYmKj4+HglJiaqbdu2+fYDAADu6dSpU+rSpYvq16+v7t27Kzk5WZLUv39/dkYtg64e4ZaYmGh7FNQPAABnKonahitQhCtjUlJSlJ2drZCQELv2kJAQHTt2zCnXSEpKsn29fft2hYWF2R5X/s9wZT8AAOCeRowYIW9vbyUkJCggIMDW/uijj2rDhg0mRgZ3cNNNN2nmzJm66aabzA4FAFCGlERtwxWYI1hGWSwWu+eGYeRpAwAA2LRpkzZu3KhatWrZtderV0+///67SVHBXWRmZuq1114zOwwAQBnlabUNRsKVMVWrVpXVas1TGT5x4kSeCrIz9OzZs8DnAADAvV24cMFuBFyulJQU+fr6mhAR3MWXX35pW/vNarXqyy+/NDkiAEBZUdK1DWcp8SJc+/bt5e/vX9KXxf/n4+Ojli1bKiYmxq49JibGbr226/HEE0/Yvg4PD7dbKyQ8PDzffgAAwD116NBBb775pu25xWJRTk6OZsyYoc6dO5sYGcx211136ejRo0pMTNTRo0d11113mR0SAKCMKInahis4dTrq4cOHtXLlSh0+fFivvfaagoODtWHDBoWFhalx48aSpHXr1jnzkm4p/qqFad3tOtHR0frHP/6hVq1aqU2bNlq6dKkSEhI0aNAgp8Q1ZcoUvf3225KkadOmadq0abJYLHl2UZsyZYpTrgcAAFxnxowZ6tSpk3bv3q3MzEyNGjVKBw4cUGpqqrZt22Z2eChhiYmJCgsLsz2/8uur+wEAPFtZr224gtOKcLGxsYqKilK7du20detWTZ48WcHBwdq/f7+WL1+ujz76yFmXcltBQUHy9/fXuOmzSuya/v7+CgoKKtIxjz76qE6dOqVXXnlFycnJatKkidatW6c6deo4La6rE7SrC3AkZgAAeIabb75Z+/fv16JFi2S1WnXhwgU99NBDGjJkiGrUqGF2eDDB1Xlefq8DADwXtQ3XcVoRbvTo0Zo0aZKio6MVGBhoa+/cuXOZWaw1NDRUmzdvVmpqaoldMygoSKGhoUU+bvDgwRo8eLALIvqfxMREjRkzxjYqTro8BZURcAAAeIZLly4pMjJSS5Ys0YQJE8wOB27kWoU4CnAA4PmobbiO04pwP/30k95555087dWqVdOpU6ecdRm3FxoaWqwbp7SaMmUKRTd4vPvvv1+ff/652WEAQInz9vbWzz//7Na7jME8FNwAoPSituEaTivCVa5cWcnJyXYL70vS3r17+YcD4NEowAEoy3r37q0VK1Zo6tSpZoeC/y8tLU1xcXFmh+G2IiIi2AgOAOCWnFaE69Wrl1544QV9+OGHtl2ztm3bppEjR6p3797OugwAAABKUGZmppYvX66YmBi1atVK5cuXt3t99uzZJkVWdsXFxal79+5mh+G21q1bp6ZNm5odBgAAeTitCDd58mT17dtXoaGhMgxDN998s7Kzs9WrVy+9+OKLzroMAAAAStDPP/+sFi1aSJJ+++03u9eYpmqOiIgIrVu3zuwwJF0uCA4bNkzz5s1TRESE2eFIktvEAQDA1ZxWhPP29taaNWs0ceJE/fDDD8rJyVHz5s1Vr149Z10CAFyuSZMm+vnnnx3qBwCl1f79+9WkSRN5eXlp8+bNZoeDq/j7+7vdSK+IiAi3iwkAAHfj5ewT3njjjXrkkUf08MMP68KFCzp9+rSzLwEALuNIAa4o/QDAEzVv3lwpKSmSLud2ZWmTLQAAAFdxWhFu+PDhWrFihSQpOztbHTt2VIsWLRQWFqYtW7Y46zIAAABwscqVKys+Pl6SdPToUeXk5JgcEQAAgOdzWhHuo48+UrNmzSRJ//73v3XkyBH9+uuvGj58uMaOHeusy8DDfPPNNwoLC7M9vvnmG7NDAhxWrVq1Ap8DQGn18MMPq2PHjgoPD5fFYlGrVq1044035vsAAACAY5y2JlxKSoqqV68u6fKORD179lT9+vXVr18/zZs3r0jnWrhwoWbMmKHk5GQ1btxYc+fOVfv27fPtu2XLFnXu3DlP+8GDB9WwYcOiv5HrlJSUpNTU1BK7XlBQkEJDQ0vsekURFhaWp61Xr16SpMTExJIOByiykydPFvgcAEqrpUuX6qGHHrItuj9gwAAFBgY65dyenOcBAFBWUNtwDacV4UJCQvTLL7+oRo0a2rBhgxYuXChJunjxoqxWq8Pnef/99zV8+HAtXLhQ7dq105IlSxQVFaVffvlFtWvXvuZxhw4dUsWKFW3PzRixkpSUpE6dOik9Pb3Erunn56ctW7Y4fLNu3bpVM2bM0J49e5ScnKy1a9eqR48eTo/r6gLcvffeqy+++MLudQpxcEcVKlTQ+fPnHeoHAKVZt27dJEl79uzRs88+W2gR7o8//lDNmjXl5XXtiRaenOcBAFBWUNtwHacV4Z588kn17NlTNWrUkMVi0d133y1J2rlzZ5E+qZw9e7b69eun/v37S5Lmzp2rjRs3atGiRZoyZco1jwsODlblypWv6z1cr9TUVKWnp+vvt3VTtcAgl1/v5LlUffj9BqWmpjp8o164cEHNmjXTk08+qYcfftglcV055XTjxo26+eabJUmLFi3SL7/8oq5du9r6XeuTb8AsLVu2VGxsrEP9AKAsWLlypUP9br75Zu3bt6/AKaqenOcBAFBWUNtwHacV4caPH68mTZooMTFRf//73+Xr6ytJslqtGj16tEPnyMzM1J49e/L0j4yM1Pbt2ws8tnnz5kpPT9fNN9+sF198Md+pC7kyMjKUkZFhe3727FmH4nNUtcAghd4Q4tRzOktUVJSioqJceo3cKaeSbAW4/J736tWL0XBwO44U4IrSDyWnpIfMe4K4uDi7/8JeWZn2UFIMwyjw9dKS5wEAUFaU9dqGKzitCCdJjzzySJ62Pn36OHx8SkqKsrOzFRJi/48cEhKiY8eO5XtMjRo1tHTpUrVs2VIZGRl666231KVLF23ZskUdOnTI95gpU6ZowoQJDseF4rn33nvzbY+MjNSmTZtKOBoApVlSUpI6duxo94c3/mfYsGFmh+CWfH19FRsbSyGuhJDnAQCAss6pRbgLFy4oNjZWCQkJyszMtHutKH8AWCwWu+eGYeRpy9WgQQM1aNDA9rxNmzZKTEzUzJkzr5mcjRkzRtHR0bbnZ8+ezXcTAVyfL774QosWLcrTTgEOgLOlpqYqIyNDAdYqslq8zQ4HHiDbuKSLGaeKNO0BzkGeBwAAyiqnFeH27t2r7t276+LFi7pw4YKCgoKUkpKigIAABQcHO1SEq1q1qqxWa55PQ0+cOJHnU9OC3HHHHXr77bev+bqvr69tuiyc75133rFNSf3ll1/spqD+8ssvdv0Ad9OlSxd99dVXDvWD+7FavFXOy8fsMOAJcswOoOwhzwMAAGXdtbevKqIRI0bovvvuU2pqqvz9/fXdd9/p999/V8uWLTVz5kyHzuHj46OWLVsqJibGrj0mJkZt27Z1OJa9e/eqRo0aRYofznPlZgtdu3ZVWFiYunfvrrCwMNumDFf3A9yFo2sHscYQANi71mi2XOR5AACgrHPaSLh9+/ZpyZIlslqtslqtysjI0I033qjp06erT58+euihhxw6T3R0tP7xj3+oVatWatOmjZYuXaqEhAQNGjRI0uUpBklJSXrzzTclXd5Vq27dumrcuLEyMzP19ttv6+OPP9bHH3/srLeGYkhMTLSb+vHTTz/leR1wR/Hx8U7tBwBlRWEbM0jkeQAAoGxzWhHO29vb9gloSEiIEhIS1KhRI1WqVEkJCQkOn+fRRx/VqVOn9Morryg5OVlNmjTRunXrVKdOHUlScnKy3fkyMzM1cuRIJSUlyd/fX40bN9Z//vMfde/e3VlvrVQ5f/683S558fHx2rdvn4KCglS7dm2nXWf9+vWyWCy69dZbtXfvXlt78+bNtW/fPq1fv94jdzJB6Xfq1Cmn9gMAT/fUU0/ptddeU2BgoF37hQsXNHToUL3xxhuSLi85UbNmzQLPRZ4HAEDx1K1bV0ePHnWoX1lQUrUNZ3NaEa558+bavXu36tevr86dO+ull15SSkqK3nrrLTVt2rRI5xo8eLAGDx6c72urVq2yez5q1CiNGjWquGG7xMlzqW57nd27d6tz586257kLF/fp0yfP97a4srOzNXHiRHXp0kVLly7V7t27dfz4cYWEhKhVq1Z6+umnNWnSJEVGRspqtTrlmoCzODKSoyj9AMDTrV69WlOnTs1ThEtLS9Obb75pK8I5uvmBp+d5gKdKSkpSamrJ/J3iKXL/gL/yD3n8T1BQEJsXXSUtLc20+6Uof6dcPRMtt90wDKWlpSknp+DFcdPT0yVR23AFpxXhXn31VZ07d06SNHHiRPXp00f//Oc/FRERYUvOSrugoCD5+fnpw+83lNg1/fz8FBQU5HD/Tp06ubx4sGvXLiUmJurxxx9Xx44d7aaehoWFqVevXvryyy+1a9cutWnTxqWxAChbso1LLLgPh2Qbl8wOwe2dPXvWlrCfO3dOfn5+tteys7O1bt06BQcHmxghAEclJSWpU6dOtj+sYc+RTQTLIj8/P23ZsoVC3BXi4uLcfjT277//nm+MoaGhmjhxoqTC13E9c+aMfH18ynxtwxWcVoRr1aqV7etq1app3bp1zjq1xwgNDdWWLVtK9BMmd/x04vjx45KkadOmqUuXLlqwYIEaNGigQ4cOaf78+Zo+fbpdPwBwlovZTBMGnKVy5cqyWCyyWCyqX79+ntctFosmTJhgQmQAiio1NVXp6en6+23dVC3Q8T9yUXadPJeqD7/foNTUVLf7e9NMERERptU6zp8/r549e8pisejxxx+32yn8iSee0Jo1a2QYhj744ANVqFAhz/G5H6zVrl270F3EIyIitGHjRp0+fbrIcfr4+MjLq+h7gLpjbcMVnFaEi4+PV1ZWlurVq2fX/t///lfe3t5lZl5yaGhombhxClKtWjVJlwuzK1assP0P2KJFC61YsUKPPPKIvv/+e1s/wJ14e3vr0qXCR8h4e3uXQDQoqgBrFVkt/NugcNnGJYq2hdi8ebMMw9Df/vY3ffzxx3afTvv4+KhOnTqFrgEHwL1UCwxS6A0hZocBeCx/f/8iL7flTM2aNdOPP/6oNWvWqHPnztq8ebM6d+5sK8A1a9bsmrPN0tPTFR8fL39/f7vR7dcSERHh7PAhJxbh+vbtq6eeeipPEW7nzp1avny5tmzZ4qxLwc0VNiQ093VPHDqK0s+RAlxR+qFkWS3eKuflY3YY8ARMWy5Ux44dJV3+oLV27dqFTl0BAACu9cUXX+jee+/Vjz/+qM2bN0uS7b/NmjXTF198YWZ4cEDRxwhew969e9WuXbs87XfccYf27dvnrMvAA6SkpEiSvv/+e/Xr10979uzR+fPntWfPHvXr10+7d++26wcAANzL/v37bYs2nzlzRj/99JP279+f7wMAAJScL774QgcPHtQdd9wh6XLN5eDBgxTgPITTRsJZLBbbxgxXOnPmjLKzs511GXiAkJDLQ9xHjx6tNWvWqEePHrbXateurRdeeEHTpk2z9QMAAO7l1ltv1bFjxxQcHKxbb71VFosl3xHsFouFPA8AgBJWoUIFvfTSS+revbteeumlfNeAg3tyWhGuffv2mjJlit59911ZrVZJl3fOmjJliu68805nXQYeoHXr1goLC9Pu3bs1cOBAvfjii7bXnn76aW3ZskW1a9dW69atTYwSAABcS3x8vG3t1vj4eJOjAQAAKB2cVoSbNm2aOnbsqAYNGqh9+/aSpG+++UZnz57V119/7azLwANYrVaNGzdOTz/9tL788ku713ILckuXLrUVawEAgHupU6dOvl8DAACg+JxWhGvcuLH279+vBQsW6Mcff5S/v7969+6tZ555xm43LZQNTz/9dKGvJyYmllA0gOO6deumDRs2ONQPAMqCzz//PN92i8UiPz8/RUREKDw8vISjAgAA8DxOKcJdunRJkZGRWrJkiV599VVnnBIebM2aNbavFy9erKCgIB0/flwhISFKTU3VoEGDbP0ef/xxs8IE8nXs2DGn9gMAT9ejR49814TLbbNYLLrzzjv16aef6oYbbjApSgAAAPfnlCKct7e3fv75Z7aul5SUlKTU1NQSu15QUJBCQ0NL7HqOGD16tO3re+65p8B+FOHgbhzdzZldnwGUFTExMRo7dqwmT55sW891165devHFFzVu3DhVqlRJAwcO1MiRI7VixQqTo3Wtks7zPEFcXJzdf2HP3XL1k+e4f+EY7hVQ23ANp01H7d27t1asWKGpU6c665QeJykpSR07dlRGRkaJXdPX11exsbEO36xTpkzRJ598ol9//VX+/v5q27atpk2bpgYNGjg9trp16+bbHhoaqqSkJKdfDwAAON+zzz6rpUuXqm3btra2Ll26yM/PT08//bQOHDiguXPn6qmnnjIxStdLSkpS586dlZaWZnYobmnYsGFmh+CW/P39tXnzZrf5w/LD7wtfcgMAqG24jtOKcJmZmVq+fLliYmLUqlUrlS9f3u712bNnO+tSbis1NVUZGRkKsFaR1eLt8utlG5d0MeOUUlNTHb5RY2NjNWTIEN12223KysrS2LFjFRkZqV9++SXPv9n1Onr0aL7tFOAAAPAchw8fVsWKFfO0V6xYUUeOHJEk1atXTykpKSUdWolKTU1VWlqaJo56TuFhYWaHAw8Qn5iocdNnFSlXd7W/39ZN1QJZrxuFO3kulaJtGUZtw3WcVoT7+eef1aJFC0nSb7/9ZvdaWZumarV4q5yXj+svlFP0Q65ecH7lypUKDg7Wnj171KFDB6eENXXqVNuU1A0bNtgtYH/l9cvyqEl4hq5du2rjxo3XfA4AZUHLli31/PPP680331S1atUkSSdPntSoUaN02223SZL++9//qlatWmaGWWLCw8LUqF6E2WEAxVItMEihN4SYHQYAD1HWaxuu4LQi3ObNm511KpSgM2fOSJJTd7B9/PHHbUW4AQMGSMp/CirrwcHdXV1wowAHoCxasWKFHnjgAdWqVUthYWGyWCxKSEjQjTfeqM8++0ySdP78eY0bN87kSAEAQFnlitqGKzitCJcrLi5Ohw8fVocOHeTv72/bNQvuxzAMRUdH684771STJk2ceu7ExESFXTFV4+oCXGJiolOvBwAAXKNBgwY6ePCgNm7cqN9++02GYahhw4a6++675eXlJenyDqplRTw5DBzEvQIAJcOVtQ1nc1oR7tSpU+rZs6c2b94si8Wi//73v7rxxhvVv39/Va5cWbNmzXLWpeAkzzzzjPbv369vv/3WJedPTEzUmjVr7HZLnTp1KiPgAADwMBaLRd26dbNbYqKsGjednBYAAHfi6tqGMzmtCDdixAh5e3srISFBjRo1srU/+uijGjFiBEU4NzN06FB9/vnn2rp1q0vXcHn88ccpugEA4GHmzZunp59+Wn5+fpo3b16BfcvarphszABH5W7MAABwnZKqbTiL04pwmzZt0saNG/O86Xr16un333931mVwnQzD0NChQ7V27Vpt2bJF4eHhZocEAADczJw5c/T444/Lz89Pc+bMuWY/i8VS5opwbMwA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6fnnn9evv/5qxikBAABQSVy5ckWpqamKiIiwKY+IiNCePXtK1MaKFSvUq1cv+fr62pRfunRJvr6+atKkiR555BGlpaXdsp38/Hzl5ubabAAAAJWBKUm4kirjQqwAAACoxM6cOaOCggJ5e3vblHt7e+vkyZO3PT47O1sbN24sMq9f69atlZiYqPXr1yspKUlubm4KDw/XkSNHbtpWXFycdZSdp6enmjZtWraLAgAAMFmFJuEAAABw57JYLDb7hmEUKStOYmKi7rrrLg0YMMCmvEuXLnrmmWcUFBSkrl276qOPPlLLli21cOHCm7Y1adIk5eTkWLfjx4+X6VoAAADMVq454QAAAID69evLycmpyKi3U6dOFRkd90eGYWjlypUaMmSIXFxcblm3Ro0a6tix4y1Hwrm6upZomhQAAICKxkg4AAAAlIuLi4uCg4OVkpJiU56SkqKwsLBbHrtjxw799NNPGjFixG3PYxiG0tPT1ahRo3LFCwAA4AiMhAMAAGWSlZWlc+fOVci5vLy85OPjUyHnQtnExsZqyJAhCgkJUWhoqJYtW6bMzExFR0dLuvaYaFZWlt59912b41asWKHOnTurTZs2RdqcMWOGunTpohYtWig3N1cLFixQenq63nrrrQq5JgAAADOVOwlXUFCg3bt3q127drr77rtvWdfX11c1a9Ys7ykBAICDZWVlqUePHvrXv/5VIedzd3fXF198UepEXEJCgubMmaPs7GwFBgYqPj5eXbt2tVOU1VtUVJTOnj2rmTNnKjs7W23atNGGDRusq51mZ2crMzPT5picnBytXr1ab775ZrFtXrhwQc8995xOnjwpT09PtW/fXjt37lSnTp3sfj0AAABmsxgmLFnq5uamQ4cOyd/f34yYKlxubq48PT2Vk5MjDw8PR4cDAIBD5OXlKSMjQ/7+/nJzc7tl3e+//179+vXTqy//Vf52Xn0y4/hxTZ09Txs2bFDbtm1LfFxycrKGDBmihIQEhYeHa+nSpXr77bd18OBBNWvWrERt3Oozof9QNXCfAABAadmr/2DK46ht27bV0aNHq2wSDgAAlI1/06YKaHGfo8Mo1vz58zVixAiNHDlSkhQfH6/Nmzdr8eLFiouLc3B0AAAAqG5MWZjhtdde04QJE/TZZ58pOztbubm5NhsAAEBFunLlilJTUxUREWFTHhERoT179jgo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",
      "text/plain": [
       "<Figure size 1500x700 with 6 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3, 2, figsize=(15,7))\n",
    "\n",
    "sns.boxplot(x = 'strength', y = 'length', hue = 'strength', ax=ax1, data=data)\n",
    "sns.boxplot(x = 'strength', y = 'lowercase_freq', hue = 'strength', ax=ax2, data=data)\n",
    "sns.boxplot(x = 'strength', y = 'uppercase_freq', hue = 'strength', ax=ax3, data=data)\n",
    "sns.boxplot(x = 'strength', y = 'digit_freq', hue = 'strength', ax=ax4, data=data)\n",
    "sns.boxplot(x = 'strength', y = 'special_char_freq', hue = 'strength', ax=ax5, data=data)\n",
    "plt.subplots_adjust(hspace=0.8)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a893d6af-f0bd-40eb-a4bc-9121af8482b8",
   "metadata": {},
   "source": [
    "## Feature Importance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "774b14d2-ab17-442c-9230-3bb764ffd1d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_dist(data,feature):\n",
    "\n",
    "    plt.figure(figsize=(10,8))\n",
    "    plt.subplot(1,2,1)\n",
    "    sns.violinplot(x='strength', y=feature, data = data)\n",
    "\n",
    "    plt.subplot(1,2,2)\n",
    "    sns.distplot(data[data['strength']==0][feature], color='red',label=\"0\", hist=False)\n",
    "    sns.distplot(data[data['strength']==1][feature], color='blue',label=\"1\", hist=False)\n",
    "    sns.distplot(data[data['strength']==2][feature], color='orange',label=\"2\", hist=False)\n",
    "    plt.legend()\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1dc7ae02-a3b0-4750-a1c8-f758231b866c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "from warnings import filterwarnings\n",
    "filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d2e733d5-cf44-4047-8286-9e5743053b13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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T3/6UydVBwDoCFocpHbu3NmWdQAA4DA5OTmSLv2B7+DBg/Lz87Pu8/Pz08CBA5WcnOys8gAAHUCLg9Tw4cOtj/Py8hQdHV1vtr7am3cBAHCm2j/+PfDAA/rd736n4OBgJ1cEAOho7JpsIiYmRj/88EO97dy8CwBwJWlpaYQoAECbsGv689p7oS7HzbsAAGebMGGC0tPTFRwcrAkTJjTZdvPmze1UFQCgozEVpOrevPub3/yGm3cBAC4nJCTE+se+kJAQJ1cDAOioTAUpbt4FALi6tLS0Bh8DAOBIpoIUN+8CANzJhQsXZBiGdQTFiRMntGXLFt1www1KSEhwcnUAAHdm12QT3LwLAHAH48aN07p16yRJZ8+e1c9+9jO9/PLLGjdunFauXOnk6gAA7syuySYau3nXYrEoICBA1157rSZNmqS+ffu2qjgAAFpj//79euWVVyRJf/7znxUREaGcnBxt2rRJTz75pB566CEnVwgAcFd29UgFBwdrx44d2r9/v/WG3pycHO3YsUNVVVXauHGjBg4cqE8++cShxQIAYEZZWZmCgoIkSdu3b9eECRPk5eWlm266SSdOnHBydQAAd2ZXkIqIiNCkSZP0zTffaNOmTdq8ebOOHTum//7v/9Y111yjw4cPa8qUKXrsscccXS8AAC127bXX6p133lF+fr4+/PBD631RRUVFDFEHALSKXUFqzZo1mjdvnry8/nW4l5eX5s6dq9WrV8tisWjOnDn68ssvHVYoAABmPfnkk0pOTtZVV12lIUOGKD4+XtKl3qlBgwY5uToAgDuz6x6pqqoqffXVV7ruuutstn/11Veqrq6WJAUEBDT4pb0AALSX//iP/9Att9yigoICDRw40Lp91KhRuvvuu51YGQDA3dnVI3X//fdr2rRpeuWVV7R792598skneuWVVzRt2jRNnjxZkpSVlaX+/fs7tFgAAMyKiIjQoEGDbEZR/OxnP9P111/fouN37dqlsWPHKioqShaLRe+8806T7TMzM2WxWOotX331VWveBgDAxdjVI/XKK68oPDxcS5Ys0ffffy9JCg8P1yOPPGK9LyohIUF33HGH4yoFAMCk8+fP68UXX9Rf/vIXFRUVqaamxmb/N99806LnGDhwoB544AHdc889LX7tI0eO2NyH1aNHj5YXDgBweXYFKW9vby1atEiLFi1SSUmJJNW7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45qaGkmX7m8aMmRIveevy9fX1/rYYrHYHG8YhnVbLcMwWvxe6j537fPXPjcAoOOpqamRt7e3srOz611vunTpYn3c0PXh8uuLo64/l1/bAFdBkALagMVi0c0336ybb75ZTz75pHr37q0tW7bIz89P1dXVzR4fHh6uK6+8Ut98843uu+8+u+u4/vrr9de//tVm2759+2zWW1oTAKDjGzRokKqrq1VUVKRhw4bZ9RwhISEKDw/XX//6V+tzVFdXKycnx+brNrj+wN0RpAAH++yzz/SXv/xFCQkJCgsL02effaYffvhB/fr108WLF/Xhhx/qyJEj6tatm0JCQhp9nsWLF+vhhx9WcHCwEhMTVV5ern379unMmTNKSkpqUS1z587VrbfeqtTUVI0dO1Y7duzQBx98YPNXwquuukq5ubk6cOCAevbsqaCgIPn7+7f6PAAA3M91112n++67T5MnT9bLL7+sQYMG6dSpU9qxY4cGDBigMWPGtOh55s6dq5SUFF177bW6/vrr9fvf/15nzpypd/357LPPdPz4cXXp0kWhoaFt9baANsE9UoCDBQcHa9euXRozZoyuu+46PfHEE3r55ZeVmJioGTNmqG/fvho8eLB69OihTz75pNHnmT59ul5//XWlp6drwIABGj58uNLT0xUTE9PiWm6++WatWrVKqampGjhwoLZt26ZHHnlEAQEB1jb33HOP7rjjDo0cOVI9evTQW2+91ar3DwBwb2lpaZo8ebIeffRR9e3bV3fddZc+++wzRUdHt/g5HnvsMf3iF7/Q5MmTFR8fry5dumj06NE215/k5GR5e3vrhhtuUI8ePZSXl9cWbwdoMxbDzIBVAG5vxowZ+uqrr/Txxx87uxQAgIeoqalRv379dO+99+rZZ591djmAQzC0D+jgli5dqttvv12dO3fWBx98oLVr19p8sS8AAI524sQJbd++XcOHD1d5ebmWL1+u3NxcTZo0ydmlAQ5DkAI6uL/+9a9asmSJzp07p6uvvlqvvvqqpk+f7uyyAAAdmJeXl9LT05WcnCzDMBQbG6uPPvpI/fr1c3ZpgMMwtA8AAAAATGKyCQAAAAAwiSAFAAAAACYRpAAAAADAJIIUAAAAAJhEkAIAAAAAkwhSAAAAAGASQQoAAAAATCJIAQAAAIBJBCkAAAAAMOn/A6A14VWilDCkAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "get_dist(data, 'length')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ff8f7da4-bd6f-4b66-91a2-d99ede978b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA04AAAKnCAYAAACxnB1/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdd3wUdf4/8NfMtmRTSSCUECD0XgRRrFgOD3s7Ob2fKJZT8fQUPQW909M7RU9PUREsfG13tju7p6gIAqKiVEF6JwRCSEjfvjO/P2ZnsyFtdzOzs+X1fDzy2LBl9k0Ju699fz7vEWRZlkFEREREREStEo0ugIiIiIiIKN4xOBEREREREbWDwYmIiIiIiKgdDE5ERERERETtYHAiIiIiIiJqB4MTERERERFROxiciIiIiIiI2sHgRERERERE1A6z0QUYQZIkHDx4EFlZWRAEwehyiIhShizLqKurQ48ePSCK/OxOxdclIiLjhPvalJLB6eDBgygqKjK6DCKilFVSUoKePXsaXUbc4OsSEZHx2nttSsnglJWVBUD5w8nOzja4GiKi1FFbW4uioqLg/8Ok4OsSEZFxwn1tSsngpC6DyM7O5gsUEZEBuBytKb4uEREZr73XJi4wJyIiIiIiageDExERERERUTsYnIiIiIiIiNqRknuciIiIiIhIIcsyfD4f/H6/0aXowmQywWw2d3h/LYMTEREREVGK8ng8OHToEBwOh9Gl6Mput6N79+6wWq1RH4PBiYiIiIgoBUmShD179sBkMqFHjx6wWq1JN/VUlmV4PB4cOXIEe/bswYABA6I+ATuDExERERFRCvJ4PJAkCUVFRbDb7UaXo5v09HRYLBbs27cPHo8HaWlpUR2HwyGIiIiIiFJYtB2YRKLF7zH5/5SIiIiIiIg6iMGJiIiIiIioHQxORERERERE7WBwIiIiIiKihDNv3jwUFxcjLS0NY8eOxbfffqvr8zE4ERERERFRQnn33Xdxxx134P7778e6detw6qmnYvLkydi/f79uz8lx5EREREREBMgyYNSJcO12IIJzSD311FO4/vrrccMNNwAA5syZgy+//BLz58/H7NmzdSmRwYmIiIiIiJTQlJlpzHPX1wMZGWHd1ePxYM2aNZg5c2aT6ydNmoTvv/9ej+oAcKkeERERERElkIqKCvj9fnTt2rXJ9V27dkVZWZluz8uOExERERERKcvl6uuNe+4ICccs7ZNludl1WmJwIiIiIiIiZY9RmMvljNS5c2eYTKZm3aXy8vJmXSgtcakeERERERElDKvVirFjx2LRokVNrl+0aBFOOukk3Z6XHSciIiIiIkooM2bMwNVXX41x48ZhwoQJeOmll7B//37cfPPNuj0ngxMRERERESWUKVOmoLKyEg8//DAOHTqE4cOH4/PPP0fv3r11e04GJyIiIiIiSjjTp0/H9OnTY/Z83ONERERERETUDgYnIiIiIiKidjA4JTGv14sHHngAy5YtM7oUIiIiosQiy4DXa3QVFEcYnJLY9u3bsXz5cjz44INGl0JERESUWO67D8jMBNatM7oSihMMTklMkiSjSyAiIiJKTP/+N+DxAO+8Y3QlFCcYnIiIiIiIQpWUAAcOKN9zywMFMDgREREREYX6/vvG71evBurrjauF4gaDExERERFRqNDg5Pc3/TWlLAYnIiIiIqJQalDq1Em55HI9AoNTUuNwCCIiIqIINTQ0TtK7/XblksEp7ixfvhwXXHABevToAUEQ8NFHH+n+nAxOSczv9xtdAhEREVFiWbNGWZ7Xowdw1VXKdatXK+d1orjR0NCAUaNGYe7cuTF7TnPMnolijsGJiIiIKEK7dimXI0YAPXsq37vdyoCIrCzj6qImJk+ejMmTJ8f0ORmckhiDExEREVGEjhxRLgsKALsdSEsDXC6goiLpg5MsAw6HMc9ttwOCYMxzh4vBKYkxOBERERFFSA1OXbool507K+d0qqwEiouNqysGHA4gM9OY566vBzIyjHnucHGPUxJjcCIiIiKKUHm5cllQoFzm5yuXFRXG1ENxgx2nJObz+YwugYiIiCixtNRxApSOU5Kz240716/dbszzRoLBKYmx40REREQUoWODUwp1nAQh/pfLGYnBKYkxOBERERFF6NileinUcUok9fX12LlzZ/DXe/bswfr165GXl4devXrp8pwMTkmMS/WIiIiIIpTCHadEsnr1apxxxhnBX8+YMQMAcM011+C1117T5TkZnJIYO05EREREEWhoAJxO5fsU3OOUSCZOnAg5xicl5lS9JMbgRERERBQBdZleWlrjXG52nCiAwSmJMTgRERERRSB0mZ56Nla148TglPIYnJKYJElGl0BERESUOI7d3wQ0dpy4VC/lMTglMXaciIiIiCKgLtULDU6hHacY76mh+MLglMTYcSIiIiKKgNpxUkeRA43Bye0GHI7Y10Rxg8EpiYV2nGI9dYSIiIgo4bS0VC8jA7Bale+5zymlGRqcli9fjgsuuAA9evSAIAj46KOP2n3MsmXLMHbsWKSlpaFv37544YUX9C80QYV2nBiciIiIiNrR0lI9QeBIcgJgcHBqaGjAqFGjMHfu3LDuv2fPHpx77rk49dRTsW7dOtx33324/fbb8f777+tcaeJjcCIiIiJqR0tL9QCOJCcABp8Ad/LkyZg8eXLY93/hhRfQq1cvzJkzBwAwZMgQrF69Gk8++SQuu+wynapMXAxLRERERBFoaakewI4TAUiwPU4//PADJk2a1OS6c845B6tXr4bX6231cW63G7W1tU2+UsHy5cuD3zNEEREREbWjpaV6ADtOBCDBglNZWRm6du3a5LquXbvC5/Ohoo1/yLNnz0ZOTk7wq6ioSO9S40KqBEQiIiIiTagdJbXDpOJJcOPK7NmzcfzxxyMrKwsFBQW4+OKLsW3bNt2fN6GCEwAI6lmcA9ROyrHXh5o1axZqamqCXyUlJbrWGI/YcSIiIiJqg98PNDQo3+fkNL2NJ8GNK8uWLcOtt96KlStXYtGiRfD5fJg0aRIa1L8/nRi6xylS3bp1Q1lZWZPrysvLYTabka/+g26BzWaDzWbTu7y41lawJCIiIkp5dXWN32dnN70tK0u5rK+PXT3Uqi+++KLJr1999VUUFBRgzZo1OO2003R73oQKThMmTMCnn37a5LqvvvoK48aNg8ViMaiqxCCKCddcJCIiIoodNThZLMCxH7hnZCiXOnc0DCfLgN+gk/ya7Mro9yjU1NQAAPLy8rSsqBlDg1N9fT127twZ/PWePXuwfv165OXloVevXpg1axZKS0vxxhtvAABuvvlmzJ07FzNmzMCNN96IH374Af/3f/+Ht99+26jfQlwL7TKx40RERETUBnVv+LHdJgDIzFQuk73j5HcA/8k05rmvqAfMGRE/TJZlzJgxA6eccgqGDx+uQ2GNDA1Oq1evxhlnnBH89YwZMwAA11xzDV577TUcOnQI+/fvD95eXFyMzz//HHfeeSeef/559OjRA88++yxHkYeBwYmIiIioDW0Fp1TpOCWgP/zhD9iwYQNWrFih+3MZGpwmTpzY5tCC1157rdl1p59+OtauXatjVURERESUctTgpO5nCpUqHSeTXen8GPXcEbrtttvwySefYPny5ejZs6cORTWVUHucKDLsMhERERGFSd3jlIgdJ1kG3noLGD0aGDYs+uMIQlTL5WJNlmXcdttt+PDDD7F06VIUFxfH5HkZnIiIiIiIEnmP03PPAX/8I1BcDOzebXQ1urv11lvx1ltv4eOPP0ZWVlZw6nZOTg7S09N1e16OWkti7DgRERERhSmc4BSvHacHH1Qu9+wxto4YmT9/PmpqajBx4kR07949+PXuu+/q+rzsOBERERERqUv1WtrjpC7Vq69XlsXF04fTmzcD1dWNv3a7m49TTzJtzUjQEztOSYwdJyIiIqIwhdNx8vuVYBJPXnih6a8PHTKmjhTA4JTEGJyIiIiIwhTOOHIg/pbrffJJ01+XlhpTRwpgcCIiIiIiamupntncuPwt3gZElJcrl4WFyiWDk24YnJIYO05EicHn82HRokWoU1+0iYgo9trqOAHxOZLc6VS+AGDkSOWSwUk3DE5ERAb75ptv8Mgjj2D+/PlGl0JR+utf/wpBEJp8devWzeiyiCgS7QWneBxJfvSocmkyAYMHK98zOOmGwSmJseOUnNavX4/FixfD5XIZXQppZHfgnBvLli0zuBLqiGHDhuHQoUPBr40bNxpdEhFFoq2lekB8jiRXg1NeHtCzp/L9wYMRH8aoKXWxpMXvkePIiRJIVVUV7rjjDgDAH/7wB1x++eXGFkREQWazmV0mokQW7lK9eOo4VVYql/n5QI8eyvcRdJwsFgsAwOFw6Hri2HjgcDgANP6eo8HglMTYcUo+JSUlwe/3799vYCVEdKwdO3agR48esNlsOOGEE/Doo4+ib9++RpdFROEKd6levHacohgOYTKZkJubi/LAgAm73Z507x9lWYbD4UB5eTlyc3NhMpmiPhaDE1ECKSsrC35/iOdpIIobJ5xwAt544w0MHDgQhw8fxt///necdNJJ2LRpE/Lz85vd3+12wx1yLpha9Q0bERmnvaV68d5xCg1OEZykV+2Uq+EpWeXm5nZ4VQCDE1ECCQ1Lhw6VtXFPSkSpsMY8WU2ePDn4/YgRIzBhwgT069cPr7/+OmbMmNHs/rNnz8ZDDz0UyxKJqC1ud+OJbRNxOEReXuNSPZcLqK4GOnUK6xCCIKB79+4oKCiA1+vVp06DWSyWDnWaVAxORAlE7ThJ5jQcPlwGSZIgipzxkiySbXlEKsvIyMCIESOwY8eOFm+fNWtWk0BVW1uLoqKiWJVHRMcKPR1Eex2neFqqF9pxSktTAtTRo0rXKczgpDKZTJqEi2TGd1xECUTZ4yTAn9UNXq836dvqRInK7XZjy5Yt6N69e4u322w2ZGdnN/kiIgOpwcluV05225J47zgBPAmuzhiciBKE0+nElq1b4c/oDH+WskZ3/fr1xhZFRACAu+++G8uWLcOePXvw448/4vLLL0dtbS2uueYao0sjonCo+wxb6zYB8TkcIrTjBDA46YzBiShBbNiwAX6fD77sHvBnK+uY16xZY3BVRAQABw4cwJVXXolBgwbh0ksvhdVqxcqVK9G7d2+jSyOicLQ3UQ+Iz+EQx3acOndWLquqjKknyXGPUxKTJMnoEkhDakjyZ/eAlJYD2WLH6jVrIMsy98YkCQ6HSFzvvPOO0SUQUUeoS/XaCk6J0HGKx+WESYQdpyTGN2HJZfXq1YBohj+zABAE+LJ7oOroUezZs8fo0kgjDMBERAYJZ6leInScGJx0xeCUxNhxSh7l5eXYvXs3fFldAVGZeOMLLNdbuXKlkaURERElvnCW6sVbx0mW2XGKMQanJMaOU/J47733AADevL7B63y5RYDJgg8//DBpz7tAREQUE+Es1Yu3jpPDAXg8yvfsOMUEg1MSC+04+Xw+Ayuhjqirq8Mnn34K2ZoBX0hwgtkGT+eBOHLkCBYvXmxcgURERIkukql68RJK1G6T1doY6uKtxiTD4JTEQsPSkSNHDKyEOuKjjz6Cy+mEu+vw4DI9lafbcEAQ8fbbb3NpJhERUbQScRx56P4mdY+sWn/oCX1JMwxOSSx0+VZZWZmBlVC03G433nvvPchmG7xdBja7XbZmwJPfD/v27cMPP/xgQIVERERJwOFQLtVw1JJ4W6p37P4mgB0nnTE4JbHQ4HTo0CEDK6Foffrpp6ipqYGnYAhgsrR4H2+3EQCAf/3rX+w6ERERRUPtItntrd8nnjtOKgYnXTE4JSmfz9dkqR6DU+IpLS3FywsWAGYbvAVDW72flJ4Lb15fbN26Fe+//34MKyQiIkoSasdJ7Sq1RL3N620cymAkdpxijsEpSZWXlzf5NYNTYvH7/Xjsscfgdrng7D0BsiWtzfu7e50I2ZKOl156Cfv27YtRlURERElCDU5tdZxCQ1U8dJ3YcYo5BqcktWXLlmN+vZXjyRPIf//7X2zcuBHevOKmk/RaIVvS4OxzMrxeLx599FFOUSQiIopEOEv1rFbAElg2Hw/BpKUR6mpw4nAIXTA4Jally5YFv5dNVpSWHsCuXbsMrIjCtWfPHixYsACyxQ5X75PCfpw/txc8nQdg27ZtePPNN3WskPTCDzeIiAwSzlI9IL72ObUU9tSpeh5PfCwnTDIMTknI4XDgh5UrIQvK6GrZbAMALF261MCqKBwejyfYMXL2ORkI/N2Fy93rBMi2TLzxxhvYunWrTlWS1tShHoI6TpaIiGIrnI4T0Bis4iE4tRT24m05YZJhcEpCP/zwA7weD2SzFQAgmyyAyYJvvlnKT7TjmCzLmDNnDnbs2AFPl0Hw5xZFfhCTFc4+p8Lvl/CXv/wFVVVV2hdKmnO73UaXQESU2sLtOKUF9hy7XPrWEw41GIXWbLUqX0B8LCdMMgxOSUjtLMkmtVshwJvTC6WlB7Bz507D6qK2ffjhh/j888/hz+gMd68TWr1f2q6lsG/6GGm7lrZ4uz+7O9w9x+LIkSN48MEHm4ylp/jkCrwA84MNIiKDhNtxSk9XLp1OfesJR0vBCeCACB0xOCWZqqoqrFy5Ev70ToBoCl7vy+sDAPjyyy8Nqozasm7dOsydOxeyJR3O/mcBornV+4quGpgclRBdNa3ex9NtBLx5fbFhwwY899xzepRMGmLHiYjIYMnScQIYnHTE4JREZFnGk08+Ca/XC2/BkCa3+XJ6QrZl4YMPPsDmzZsNqpBacujQITzw4IOQZAGO/mdBtrbzn3Y4BAGuPqfAb8/HJ598gk8//bTjxyTdOAOfXLLjRERkAL+/MQglU8eJk/U0x+CURD777DN899138GUXwttlUNMbRROcxadCkmT8/ZFH4FA/WSFDuVwu/PnPf0ZdbS1cvSdAyizQ7uAmM5z9z4JsScOcOc9gw4YN2h2bNNUQePHjskoiIgOEhqBk6Dipk/XYcdIcg1OSOHDgAJ6bOxcw2+AqPgVoYTqXP6sb3N1H4GBpKebPn29AlXSs5557Drt27YKnYAi8XQZqfnzZlglnvzPhlyQ89PDDqKlpfXkfGac+8OLm8/m4bI+IKNZCp8+ltX3C+eDtidBxYnDSHINTEvD5fHj00Ufhdrng7H1Sm0u9PD3GwG/Px6efforvv/8+hlXSsZYuXYrPPvsMfns+3EXjdXsef1Y3uAuPQ2VFBZ544gkuB4tD9SEv2g0cH0tEFFvqKhy7HRDbeWusLtWLp47TscsLGZx0w+CUBN566y1s3rwZ3vx+8OUVt31n0QRX39MA0YR//OMfHFdtkLKyMvzjiScAkwXOfhObDPLQg6fbCPiye2DFihX45JNPdH0uilx9XeOLG4MTEVGMhQan9rDjlNIYnBKYLMt477338Oqrr0G2ZsLVa0JYj5PSO8HVcxyqq6tx99134/DhwzpXSqF8Ph/+9re/wdHQAGevCZDTcvR/UkGAq/g0yJY0zJ07F7t379b/OSksfr8fTmfjnsN6vtAREcVWuKPIgfjpOMly65MAGZx0w+CUoHw+H5566inMnTsXkiUNjgFnAYET3obDWzAUnoKh2LVrF266+WZO2ouhN954A5s2bVI6hJ37x+x5Zasdzj6nwuv14uGHHw6eO4iMVXfM1KPa2lqDKiEiSlHhjiIH4mc4hMulhCeAU/ViiMEpAdXV1eGee+7Bp59+Cr89Hw1DLoBkz4/sIIIAd+8T4eo9AdXV1fjjH/+IxYsX61MwBVVUVODf//43JFsWXL3D6xBqyZ9bBE/XYdi7dy9HlMcJNSjJgtjk10REFCPRdJyMXqoXuqz72Lo5VU83DE4J5sCBA7jllluwdu1aeDv1hmPwuR0674+3YAgcAybBKwn429/+hldffZXDA3T05ZdfQpIkeLqPAkzhdwi15O4xGhBN+Oyzz/h3HQfUSYdSYMkmJx8SEcVYInac1OCUlgaYjtknzaV6umFwSiDr1q3DzTffjAMHDsDdfSRc/c4ETJYOH9efU4iGIedDsmXj9ddfx8MPP8yRyDqQZRmff74QEM3wtjfEQ09mG7y5vbB3715s27bNuDoIQGOHSQ1O7DgREcVYInecWgp7DE66YXBKAJIk4YMPPsDdd9+N+gYHnMWnwdNzXIvnaor6OdJz0TD0fPiyuuGbb77BH//4R5SWlmp2fAJ++eUXlJYegLdTH00Cb0d4OyvnjFq4cKGhdVBoxym7ya+JiChGErnjxOAUUwxOcW779u2YPn06nn32WfhECxyDJus3UMCcBufAc+DpPABbt27Ftddei9dff53dJ42oIUWPE91Gyp/dHbI1E4u+/pp/vwZrDE65TX5NREQxksgdp5Zq5nAI3TA4xam6ujo888wzuOmmm7F161Z48/uhYdgl8Gd11feJRRPcfU6Bs9+Z8AhWvPrqq5h23XVYtWqVvs+bApYtWwbJlgl/ps5/h+EQRHjy+8LR0IA1a9YYXU1Kq66uBtC4VE/9NRERxUiydZw4HEI3ZqMLoKZkWcbXX3+N5+fNQ3VVFaS0XLh6T4A/u3vsihAE+PL6oD6nELaD63Dw4Cb86U9/wsSJE3HrrbeiS5cusasliZjNFsh+WdMllh0iKj/+VqsxQypIoQYl2ZIO2ZzG4EREFGuRnAA33jpOXKoXUwxOcWTfvn2YM2cO1q1bB4hmuHuOg6frMEA0tf9gPZgscBeNhze/P2z7fsDSpUux8scfcd20abj00kthNvOfTyS6di1Azc7dynkX4iA8CR7lP10GYWOpS/NkcxokcxqX6hERxVpbIeRYidBxYnDSDZfqxQGXy4WXX34Z1113PdatWwdvbm/UD78Unu4jjQtNISR7HpyDz4Wz+FQ4vTLmzZuH3//+99i4caPRpSWULl26AJIP8HuMLgUAIAaCU0FBgcGVpLaamhql+2cyQ7YowUmSJKPLIiJKHZF0nNTgZHTHqa3lhQxOumHLwECyLGPJkiV48cUXUV5eDsmWCVffE+HP7WV0ac0JAnydB6A+txdsB1Zj9+5tuO222zBp0iTccMMNfPMdBvXPSPQ0QDLbDK5G6ThlZmYhXV12QIaorq4J/nuQzTZIkoSGhgZkqWvUiYhIX9EMh0iEjpPbDXi9gMXYSb7JhMHJIJs2bcLzzz+PzZs3KwMZuo8KnBQ1zv9KzDa4+5wMb+cBSNv3A7766issXboMV175W0yZMgX2cP7TSVHB4OSqgWTPM7YYyQ/RU4+ufeIwpKeY2toayGpwMimXNTU1DE5ERLGSbMMhQj8QdToZnDTEpXoxdujQITz00EO49dZbsXnzZnjzipVleT3Hxn9oCiFlFsAx9EI4i0+DG2a8/vrr+H//7/9h4cKFXGbUivHjxwMArGUblX1OBrKUb4Xg9wZrImP4fD40NDQ0BqfAJU+CS0QUQ4k8jryl4KSGO8D4gJdkGJxipKGhAS+99BKmTp2Kb775Bv6MLmgYcj5c/c6AbEvQT5YFAb7O/VE//FK4e4zB0epaPP744/j973+vDLigJvr164czzzwTpoYKmKv3GVeI3wtb2c+wZ2TgyiuvNK4OQn1g/blsUl7kZLNyyeBERBRDidxxainsCQJgC2wJMLrOJMPgpDOfz4dPPvkEV111Fd566y14BBucfSfCMeR8SJlJsi/IZIGncAzqR1wOb+cB2LlzJ+68807cf//9KCkpMbq6uHLddddBFEXYStcCsjGdOevhTRC8Llz5298iOzvbkBpI0ThRjx0nIiLDRNtxMnL1SHuTAOOlM5ZkEmdtWAJavXo15j7/PPbu2aOM9u45Dp6uQ4Pnz0k2stUOV/Gp8BQMha3kJ3z33XdYuXIlLr74Ylx77bXcswGgZ8+eOO+88/Dpp5/CXLkLvs4DYluAzwVb2S/Izc3FZZddFtvnpmbqAmd1VwMTGJyIiGIvmo6TLCuDF4w6F2J7wSleOmNJhh0nHTidTvzzn//E3Xffjb179sLTZTDqR1weGC+enKEplJSRD+egX8PR/2x4LRl4//33ce20aVi7dq3RpcWFqVOnwmK1Iq10HeD3xfS5bQd/BvweTJ06lYM84kBD4IVPNlmbXDrUF3EiItJfNB0nwNhuDoOTIRicNLZt2zbceOON+PTTT+G356Nh2EVw9zkJsiXFRj4LAvydeqFh2CVw9xyLysqjuOuuu/DCCy/A6/UaXZ2hunTpgilXXAHBUw9b6ZqYPa9YXw7r4c0oLCzE+eefH7Pnpdape5xgUiYeyYHLep57g4godiLpOFmtjSexNzKUcKmeIRicNOL3+/HWW29h+vTpOHDgANzdRij7mIweO2000QRP91FoGHI+/LZsvPPOO7jllluwb5+BwxHiwNVXX42iXr1gPbwJprrD+j+h5EP6nhUQBODee++F1ailBdREax0n9XoiItKZLEd2AlxBiI+T4LLjZAgGJw2Ul5fjrrvuwksvvQSfKQ2OQZPhKToeEE1GlxY3pIzOaBh6ITxdBmHnzp248cbf45NPPoFs8Fhuo9hsNsyaOROCICJt77eApO+SPWvpeoiualx22WUYOXKkrs9F4WsMToFzbDA4ERHFlscD+P3K9+F0nID4CCXtdcniocYkxODUQUuXLsV1112H9evXw9upD+qHXQx/dnfD6rH/8iEy1r2NjHVvQ3QcBQCIjqPIWPc27L98aFhdAJQBGX1OhrP/WXBLAp566in8+c9/RnV1tbF1GWTo0KH47W+nQHTVwnZAv/1fYv0R2Mo2okdhIW644Qbdnocix44TEZHBQveUhrv3Nx6WwXGpniEYnKIkSRKefPJJ/PWvf0W90wVnn1Pg6ndGcCqWUQSvC6LPCdHnhAClmyNAVn7tjY9PHXydeqNh2MXwZffAd999h2nTrsPmzZuNLssQ1157bWDJ3i8Q68u1fwLJj/S930IQgJn33ou00JPikeGc6gua2nESRUAQG68nIiJ9qQHEYlG+whEP3Rwu1TMEg1OUvv76a/zvf/+D356P+qEXw9dlYONmQWqXbLXDOfAcuIpOQFV1FR555JGUHBphs9kw8957le8PrNb8+JbKnRCd1bjooou4RC8OuQIvaHLItE3ZZGFwIiKKFbXjlB7BEK94CCXtTQJkx0kXDE5RcDgceOGFFwDRDOeAsyGn8SSiUREEeLsNg6dgKEpLS/H+++8bXZEhhg0bhpNOOgnmujKY6sq0O7AkwXpoAyxWK6ZOnardcUkzzTpOUEIUgxMRUYxEMhhCZXQo8fmUvVkAO04xxuAUhTfffBNHjx6Fu/tIyNYwNxJSq9w9RkM2p+H111/H0aNHjS7HEGqwsR5cr9kxzUd3QXTX4cILLkBeXopPd4xTakCSxdDgxI4TEVHMqMEikTpOoftgGZxiisEpQqWlpXj33Xch2zLh6Tbc6HKSg9kGd+FxcDqdWLBggdHVGGLw4MEYP348zLUHIWoxnlyWYDv4MywWC6688sqOH490EQxIoRM4Tew4ERHFjPr/bSTByeiOk9olE0XA1sreeqNrTFIMThGaP38+fD4fXD3HAyH7EqhjvF0Gwm/Px8KFC7Ft2zajyzHENddcAwCwHVrf4WOZK3dDdNfivPPOQ+fOnTt8PNKHy+VSlumF7I+URQvcbnfKjuonIoopNVhEMjzJ6G5OaNhrbX+90TUmKQanCOzYsQMrVqyAL6s7fJ16G11OchFEuHudAFmW8dprrxldjSGGDRuGESNGwFxTCvg9HTqWpWoPAOC3v/2tFqWRTpxOZ5PBEAAA0QxZluF2u40piogolSRix0kNQ22FPQYnXTA4RcBkUpbTyMd8QkzaUM9ho/45p6IBAwYAAER3XYeOI7jrkJWVhW7dumlRFumkpeAkm8zB24iISGeJuMcpnLBndLhLUgxOEejbty8GDx4MS00JBA9PUKk1y5GtAIDzzjvP4EqM0727cvJk0V0f/UFkGSZ3ffBYFL9aDE6BQREufkpIRKQ/dpwoAgxOEbrgggsAWYalYofRpSQXvxfWyt0oKCjA+PHjja7GMGqHSOhAx0nwuQDJx+CUAFwuFyAec8JFkR0nIqKYScQ9TgxOhmFwitCZZ54Ju90O65FtgCwZXU7SMB/dA/g9OP/881N6qZ4WHSc1dDE4xTefzwev16ss/Q2h/prBiYgoBhK548SlejHH4BSh9PR0TJo0CYKnAaaaUqPLSRrWI1shiiImT55sdCmGys5WTqYseKP/j07wuZoci+KTIzBO9tjgpJ4Mt6GBy4GJiHSXyHuc2HGKOQanKFxwwQUAgPR930N0VBpcTYKTJdj2/whTQwUmTJiALl26GF2RodRR7FJG9CesldKVx27dulWTmkgfajBqreOkBisiItJRNB0nNZQY3XFqKzipvx8GJ00xOEWhX79+uPXWWyF6HcjY+hlMVfuNLikx+b1I37EY1sOb0KdPH9x+++1GV2S49evXAwB8WdEvs5NtmZBsWVj/88+QJC4njVfBpXjHBieRwYmIKGai2eNkdCiJZI8Tl+ppisEpSr/5zW/w97//HTaLGfadX8N6aAPAE1aGTXDXI2PL/2CuKcGJJ56I559/Hl27djW6LMOtW7cOEM2Q7B07aa0/qxtqa2qwd+9ebQojzTV2nKxNrld/zaV6REQxkMhL9dqq2egakxSDUwecfPLJeH7uXHTp0gW2A6uRtncFIPmNLivuiXWHkbHlU4jOKlx++eV45JFHkJGRYXRZhqupqcHu3bvhy+wKiB370fRlKdP51A4WxZ/gHqdjp+pxqR4RUewk8nCIcJbqseOkKQanDurfvz9eeOEFDB06FJaKHUjf9gUEL9N9a8yVu5CxbSHMkgd33XUX/vCHP6T0FL1QP/zwAwClW9RR/sBSv++++67DxyJ91NcHJiea2XEiIjJMR/Y4JcJSPXacNMXgpIH8/Hw8/fTTOOuss2CuPwz7lk8h1h8xuqz4IvlgK1mF9N3LkJlhxxNPPBEcskHKaOo33ngDEER48/t1+HiyLRO+7B5Ys2YNNmzYoEGFpLX2hkMEgxUREemnI3ucjOrmcKmeYRicNGKz2fDnP/8Z1113HUR3HTK2fArbvpWA32t0aYYz1R5CxqaPYC3biJ49e2L+/Pk47rjjjC4rrixcuBAHDx6Ep8tgyLZMTY7pLhwLAFiwYAFk7r+LO2owarbHycyOExFRzESzx8lma/rYWONSPcMwOGlIEARMnToVzz33HHr37g1r+WZk/vJB6k7d87mQtudb2LcthNlTjylTpuDll19GUVGR0ZXFFbfbjddefx0QzfD0GKXZcaXMLvDm9sKGDRuwevVqzY5L2mhtOAREBiciopiJZqmeGpzcbu3rCUckS/Xcbg4v0xCDkw5GjBiBBQsW4LrrroNV9sC+82uk7VwMwZMib4RkGebKXcj85QNYKnZg4MCBePHFF3HLLbcgPZL/mFLEJ598gsqKCri7DoVs0fbPx1OodPZefvlldp3iTDAYHXsCXFEERDODExFRLESzVC+RghNgXJ1JiMFJJxaLBVOnTsUrr7yC0aNHw1K1TwkS5VuSOvkLrlqkb/8K6buXIc0E/OEPf8D8+fMxYMAAo0uLS7W1tfjXv/4NmKzwdBuh+fElex68eX2xfft2LFmyRPPjU/TU8zg1m6oHZZ+Tk8sriIj0l4gdp3BqDr2NryeaYXDSWVFREZ5++mnce++9yLKnIW3fD7Bv+R9Ex1GjS9OWJMF6aAMyN30Ec20pJkyYgDdefx2XX345p+a14YUXXkBtbQ1cPUYBZpsuz+EuPA4QzXhu7lzU1dXp8hwUueA48mM7TgBk0YwGjiMnItJfR/Y4xXPHyWxuPLUJB0RohsEpBgRBwOTJk/Gvf/0Lv/rVr2BqOIKMzZ/AemA1IPmMLq/DxPojsG/5BLYDq9EpJxt//etf8eijj/KEtu1Yt24dPv/8c/jt+fB2Habb88hp2XD3GI3qqiq89NJLuj0PRSZ4nqaWgpPJwvM4ERHFQiJ2nMIJToLQ+HticNIMg1MM5ebm4v7778cTTzyBbl27wnZoAzI2fQRT7SGjS4uO3wvb/h+RseV/MDmO4oILLsAbb7yOiRMnQhAEo6uLa263G//85z8BCHD1ORkQ9P1R9HQbDr89D59++il+/vlnXZ+LwuNwOADR1OLfvSxa4HQ4uC+NiEhvibjHKdywp/6euFRPMwxOBjj++OPx6quvYMqUKTC562HfthC2PSsAX+Js3jPVHEDmpg9hPbwJRb2K8Oyzz+Kuu+5CVlaW0aUlhH//+984cOAAPF2HQcrorP8TCiJcfU4BIODJJ5+Ex+PR/zmpTU6ns8X9TQAAkwWSJPHviYhIbx1ZqufzAZKkfU3tCafjFHo7O06aYXAySHp6Om655Ra88MJ89O/fH9aK7cj85QOYj+6J6+ERgteJtF1LYd/+Fcw+F6655hr834IFGDlypNGlJYy9e/firbfegmTLhLtwTMyeV8roDE/XoSgpKcGbb74Zs+ellvl8Pshiy/v/ZMEUvA8REelEkhq7RtEEJ8CYrlO4wYnnctIcg5PBBg0ahBdeeAE333wzrIIf6bu+ic/R5bIMc8UOZP7yISxHd2Po0KFYsOBlTJs2DVartf3HEwBAlmU8++yz8Pv9cPU+qcX9LXpyFx4H2ZqBt95+G4cOJegS0STh9XpbX6IZuN7r5Qm0iYh0E9qJScTgFO5SPXacNMPgFAfMZjN++9vf4rVXX8Vxxx0HS/X+uBpdLrjrkL79S6Tv+RZpFgG33347nnvuORQXFxtdWsJZsWIF1q5dC29uL/hzesa+AJMFrqLj4fV4MH/+/Ng/PwV5vT7IrQWnwCQkdpyIiHQU2omJZI9T6AfGRgSncPdlMThpLi6C07x581BcXIy0tDSMHTsW3377bZv3f/PNNzFq1CjY7XZ0794d06ZNQ2VlZYyq1U9hYSH++c9/NhldnrbrG8Bv3KfOppoDyNz8Ccy1B3HSSSfhjddfx6WXXsoR41Fwu92Y+/zzgCDCXTTesDp8nYrhy+qG5cuXY+3atYbVkep8fl+rHSc1UDE4ERHpSA0UZrPyFS5BaAxPXKqXUgwPTu+++y7uuOMO3H///Vi3bh1OPfVUTJ48Gfv372/x/itWrMDUqVNx/fXXY9OmTfjvf/+LVatW4YYbbohx5fpQR5e//vrrGDNmDCxVe5Gx5VMIrprYFiLLsB76GfbtX8Eiypg5cyYeeeQRFBQUxLaOJPLuu+/icFkZ3F2HQ07LNq4QQYC71wkABDz77LN8c24QXxhL9fh3Q0Sko2hGkauMnKzH4RCGMTw4PfXUU7j++utxww03YMiQIZgzZw6KiopaXUa0cuVK9OnTB7fffjuKi4txyimn4KabbsLq1atjXLm+8vLy8MQTT+CKK66A6KxG5uZPYaouic2T+71I2/UNbAfWoKCgAM/PnYtf//rXHDHeAeXl5fj3v9+EbLHD02OU0eVAsufD02UQ9u7di08++cTocoiIiGIvmlHkKiODU6TjyBmcNGNocPJ4PFizZg0mTZrU5PpJkybh+++/b/ExJ510Eg4cOIDPP/8csizj8OHDeO+993Deeee1+jxutxu1tbVNvhKB2WzG9OnT8ec//xlWkwD7jkWwHlyv674nwVWDjC2fwlK1F2PGjMFLL72EgQMH6vZ8qeLjjz+Gx+OGq/C4mA+EaI0nUMu7//kP/H6/0eWkHFE0AWjlZznwMy6Khn+2RUSUvBKx4+T3A+rgIC7VizlDX5UrKirg9/vRtWvXJtd37doVZWVlLT7mpJNOwptvvokpU6bAarWiW7duyM3NxXPPPdfq88yePRs5OTnBr6KiIk1/H3o7++yz8fzzc9G1WzfYStcibdcSXfY9mapLkLn5U4jOalxxxRV44oknkJubq/nzpBqv14vPPvsMsjkNvvx+RpcTJFvS4Mnrh8NlZUnXsU0Eoii0+iGIEAhU7PISEekomnM4qYwKTqHPx6V6MRcXH2ce++ZAluVW3zBs3rwZt99+Ox544AGsWbMGX3zxBfbs2YObb7651ePPmjULNTU1wa+SkhgtedPQgAED8NKLL2Ls2LGwVO1DxuZPIXgcmh3fUrZJ6WiZBPz5z3/G9OnTYY5koyS16rvvvkN1dTW8nQcArZy3xyjegkEAwOV6BhBFsfXuceB6DmEhItJRInacQkNQuB0nBifNGBqcOnfuDJPJ1Ky7VF5e3qwLpZo9ezZOPvlk/OlPf8LIkSNxzjnnYN68eXjllVdaPS+NzWZDdnZ2k69ElJOTg8cff1zZ9+SqRvrOxYDU8SVWpur9SCv5EV26dMHzz8/F2WefrUG1pPr4448BAJ4ugwyupDnJng9/Rhd8//0PKC8vN7qclCKauFSPiMhQibjHSa05nEmA6u+LS/U0Y+irstVqxdixY7Fo0aIm1y9atAgnnXRSi49xOBzN3kyon8rKcXDOI72ZzWbccsstOOecc2BqOAJbyY8dOp7gqoV993LYbDY89thjGDBggEaVEgCUlJRg3bp18GX3MHaSXhs8BYMhyxI+//xzo0tJKRazGYIstXxj4Hp2fYmIdJSIS/XCnagXeh92nDRj+MeZM2bMwIIFC/DKK69gy5YtuPPOO7F///7g0rtZs2Zh6tSpwftfcMEF+OCDDzB//nzs3r0b3333HW6//XaMHz8ePXr0MOq3EVOCIGDGjBno378/rOVbYa7YEd2B/F7Ydy4G/B7cc8896NcvfvbfJIvvvvsOAJRlenHK16kYEM3tnj+NtGW1WiG01jGW/cH7EBGRThJ5qV44wYnDITRn+MeZU6ZMQWVlJR5++GEcOnQIw4cPx+eff47evXsDAA4dOtTknE7XXnst6urqMHfuXNx1113Izc3FmWeeiccff9yo34IhbDYb/va3v+HGG28E9n2PhvROkDI6h38AWUba3hUQnVW47LLLcNZZZ+lXbArbuXMnAMCfGcfnvzKZ4bfnYe++ffB6vbBY4mPqX7KzWq3BgHQsNVAxOBER6SgRg1MkNXOpnuYMD04AMH36dEyfPr3F21577bVm191222247bbbdK4q/nXv3h0PPPAA7r33Xth3LUH90AvDfqzl8GZYju7ByJEjccstt+hYZWrbvXs3ZJMVsjWzQ8ex//IhBK/yKZPgUy5Fx1FkrHsbsiUNjuGXdOj4/vQ8+OvLUVJSgr59+3boWBSe9jpOoihyqR4RkZ4ScY9TJB0nI881laQMX6pHHTN+/HhMmzYNgrseaftWhvUYwVmDtAM/IS8vDw8++CDfnOnE4/Fg37598Kd3Ajo4VlrwuiD6nBB9zsZR1ZCVX3s7vnZZsucBaOyQkf5sNhsg+VqcrCdIPljVFzwiItJHsu9xYnDSHINTEvh//+//oaioCJaaErQ6pSuEuXo/IMu4+eabkZ+fr3+BKWr//v3w+/2Q7J2MLqVd/nSlxt27dxtcSeoILolsaUCE5IeVSyaJiPSV7Ev11Bo9Hv3qSTEMTklAFEUcf/zxyklxw5gsaK49CADKY0g3Bw4cAABIabnGFhIGKT0XABLyHGeJKrh/SZaQtmsp7Js+RtqupQAAQfZzrxkRkd4SMTix42QoBqckMXbsWADKG642SX6Y6w+jX79+6NQp/jshiUySAp2EODvpbYuE1BnpHy/U4CRIPoiuGpgclRBdNcqNksTBEEREeuMeJ4oQg1OSGDVqFARBbHnZTwhTfTkg+YJBi/QTPN9YQoSRwL6pDu7FovC1tVSPHSciohhI5D1OkSzVY3DSDINTksjMzMSQIYNbP6FmgCmwTI/BSX+NISQBglMg3B17cmnST7Cj1NJkPZkdJyIi3SXiUr1IumTq6wiDk2b4LimJ9O/fv937mJxHw74vdUwidpwYnGJHnWbZ0ocdguTntEsiIr1xqR5FiO+Sksgvv/zS7n38GV0AABs3btS7nJRnMgX2NrXTBYwH6pt3Bqf4wWWTREQ6S+SlepEEJ07V0wzfJSWJw4cPKydbFdr+K/XlFAEAVq4M75xPFL0uXZSQKnrqDa6kfYJbqVGtmYiIKOkl8lI97nEyBINTkggGIaHtCW6SPQ+yxY6VK1c2Tn0jXfTo0QMAILrqDK6kfaK7FgBQWFhocCVEREQxEkn35liJ1HFicNIMg1OS+OGHHwAAcnujrwUB3twiVFdXY9u2bTGoLHVlZGQgNzcXQiCUxDPRrYQ7BiciIkoZDE4UIQanJFBXV4c1a9fCn54HoP19EepyveXLl+tcGfXs2RMmd13c73MSXew4xVp758ziObWIiHSmBgo1YETC6ODEpXqGYHBKcB6PBw888AC8Hg98+X3Deow/uztkSzreffdd7nXSWWFhISBLwT1E8Up01cJkNqOgoMDoUlKGJ7BZt6UusSyagrcTEZFOEjE4RTOO3ONJkAm/8Y/BKYFJkoTHHnsM69atg7dTH3i6DQ/vgSYLHP3PhgQRDz74ILZs2aJvoSmsX79+AACTo8LgStogSTA5K9G3uLhxEiDpzqV+aig2Hzsui+bG24mISB+pslQPALxefepJMQxOCeyFF17AkiVL4MvqBlff04B2JuqFkjK7wNHvDLg9Htx770wcOHBAx0pT17BhwwAApvpygytpneioBCQ/hg8PM3iTJtyBF1u5leDkZHAiItJXInacog1OXK6nCQanBPWf//wH//nPfyCl58LZ/6wWP7Vujz+3CM7eJ6O2tgZ/+tOfcPToUR0qTW0DBgyAxWKJ6+Ck1sbgFFttdZwgmuFyMjgREelK/X84kYJTJGGPwUlzDE4JaPHixZg3bx5kawYcA88BzFH8wAf4ugyEu/A4HDp0CDNnzoTD4dCwUrJarRg0aBBMjqOA5DO6nBaZGpTgpHbHKDZcLpcSmlo40a0smuFyuzggIkHNnj0bgiDgjjvuMLoUImqLGiYSaaleJMFJFAGzuenjqEMYnBKIJEn4z3/+g0cfnQ2YrXAMnATZmtHh43q6j4KnyyBs374dd945AyUlJRpUS6rhw4cDsgRTQ3zuczLVlyM/Px9du3Y1upSUUldXB9lkbfE22WyDLElwqpuAKWGsWrUKL730EkaOHGl0KUTUFp8PUM9nmawdp9D7MThpgsEpQZSVleHOO+/EvHnz4BMtcPT/FaT0TtocXBDg7j0Bns4DsW3bVlx//Q346KOP+Gm3RtQlcKa6MoMraU5w10H0NGDEiBEQWuh8kH6qq6shtdItlgPX19TUxLIk6qD6+nr87ne/w8svv4xOnTT6/5mI9BG6jzRZO05A42Q9BidNMDjFOVmWsXDhQkybNg0///wzvJ36oGHYJfBnadwdEES4i0+Bs9+ZcEsC5syZg3vuuQdHjhzR9nlS0MiRIyEIQlwGJ7WmUaNGGVxJavH5fKivr4dsbvnFWr2ewSmx3HrrrTjvvPNw9tlnt3tft9uN2traJl9EFEOhQYIdJwoTg1Mcq66uxgMPPIDHH38cTo8fzuLT4Op3BmRLFJ+MhMmX1wcNwy+GL6cIq1atwrRp07BkyRLdni8VZGdno2/fvjDXlzcuC4gT5kBwGj16tLGFpJj6+nrIstxucKquro5hVdQR77zzDtauXYvZs2eHdf/Zs2cjJycn+FVUVKRzhUTUhNpxMpmUr0glWnDiuQE1weAUp77//ntce+21+Pbbb+HL6o76YRfD17l/ixvJtSZb7HAOOBuuPiej3unCww8/jL/97W+oq6vT/bmT1ejRowHJBzHOzudkqitDdk4O+vTpY3QpKUUNRLKl7aV6DE6JoaSkBH/84x/x73//G2lhLvmZNWsWampqgl/cW0oUYx0ZDAE0DU6x3NrAjpOhGJziTF1dHf7xj3/gvvvuQ3VtHVxFJ8A56NeQbZmxLUQQ4O0yCPVDL4YvswCLFy/GtdOm4ccff4xtHUlCXQpnrjtkcCWNBHc9RHcdRo8axf1NMVZVVQUAkM3pLd4uW5TrGZwSw5o1a1BeXo6xY8fCbDbDbDZj2bJlePbZZ2E2m+H3+5s9xmazITs7u8kXEcVQR87hFPo4WVYGTcQKg5OhIj/5D+nC5/Phf//7H1555VXU1tbAb8+Hq+/pkNJzDa1LTsuGc/C5sJb9gsrStbj33nsxYcIE3HLLLejVq5ehtSUSddS32FBpcCWNTA6llqFDhxpcSepR9w7KVnuLt6vXc49hYjjrrLOwcePGJtdNmzYNgwcPxr333gtTNMuAiEhfkZxItiXHniPJYul4TeFgcDIUg1Mc+Omnn/D8889j3759gMkKV8/j4e06TJm/Hw8EEZ7uI+HLKYKt5Ef88MMP+Omnn3DxxRfjmmuu4SelYcjLy0N6uh1+d/xsABdcSi0MwLFXWamEVsnSSnAKXK/ej+JbVlZWsxNIZ2RkID8/nyeWJopXWnWc1GNlxmBlkCxzqp7BGJwMtG/fPsybNy+w/E2Ap8tgeArHBJfpxBvJ3gnOgefAVFOCtJJVeP/99/Hll19i2rRpuOiii2A2859TawRBQM+ehdixa4/yH18cLI0TAyGusLDQ4EpST0WFstet1Y6TOQ0QxOD9iIhIYx0NTmaz8gG3JMUulPh8jfup2HEyBN/pGqCmpgavvfYaPv74Y0iSBF92IdxF4yHZE+C8H4IAf24vNGQXwlK+FTi0Hs899xw++ugjTJ8+HSeeeCL3y7SiZ8+e2LFjBwSvs9U3zLEkumohCAK6d+9udCkpJxicLK2cwFoQIFnsDE4JbOnSpUaXQERt6ehSPUAJJU5n7EJJNCPUOVVPUwxOMeT1evHRRx/htddeR0NDPaS0HLiKxsOf0zMuOhAREU3wdhsGb+d+sJWuR8mBLZg1axbGjRuH6dOno2/fvkZXGHfUzo7oroU/HoKTuxYFBQWwqm18ipmKigpAEIPT81oiB4KTLMv8MIKISGsd7Tipj02U4MSOkyYYnGLkxx9/xHPPPYcDBw4AZhtcvU6Et8vg+NnHFC1zGty9T4S3YDBsJauwevVqXH/9Dbjwwgtwww03ICsry+gK40ZeXh4AQPA6Da5EIXqdyM/vbXQZKenIkSPK/qY2ApFktcPXUI6amhrk5ubGrjgiolSgVccJiH1wiuTcUwxOmmJw0ll5eTnmzp2L5cuXK0MWug6Du8dooI1PmhORlJ4L58BfwVRTirSSH/Hxxx/jm2+W4pZbbsY555wDMdEDogZqa5U9Ra2d9DTWZHNasCaKHUmSUFlZCSk9v837hU7WY3AiItKYVh2n0GPpLZqaGZw0xXezOvF6vXjrrbdw9dVXY/ny5fBldUPDsIvg7nVC0oWmUP6cQjQMvRiuovGobXDg8ccfx+23345du3YZXZrhjh49CgBxM/xDsqSjsvKo0WWknOrqavj9/uDkvNZIgf1P3OdERKQDBieKAjtOOli3bh2efnoO9u/fB9mSDlff0+HL65t4+5iiJYrwdhsOX14xbCU/4ZdffsGNN96ISy+9FNOmTUNGRisb4pOcetJTKU6Ck2xJh7OmEm63G7aOvHBQRBon6rX9c6B2nBiciIh0kMhL9SJ5zeY4ck0xOGmosrIS8+fPx9dffw1AgKdgKNyFY5K6w9QW2ZoBV78z4O08EGn7V+K9997DkiVLcOutt+LMM89MuQ3vVVVVgCACpvgYxqB2vo4ePcrJejHU3jmcVGpHisGJiEgHqdZx4lQ9TXCpngZ8Ph/ee+89XH311fj666/hz+iChqEXwt37xJQNTaH8OYVoGHYx3IVjcbS6Fn/7298wY8YM5YS/KcLv9+PAgQOQrG0PBIgl9Y17SUmJwZWklurqagCAbGn7U0412NbU1OhdEhFR6lE7TqkSnNhx0gSDUwfV19fjT3/6E+bOnYsGjx+uPifDMeR8SBltb/xOOaIJnh6jUD/8Enhze2HdunW4/vrrsWTJEqMri4kNGzaguroavuyeRpcS5M9RauH5ZmJLXbLZ3l43dYiIen8iItKQGiSSfakeg5OmGJw6oKKiArfffjvWrVsHb6c+aBh+GbxdBsVNRyEeybYsuAacDUf/s+GTRTz88MN47733jC5Ld4sXLwYA+PLj5/xW/swCSNZMLFu+HB628GMm2HFqZ7qico4nIXh/IiLSUKot1WNw0gSDU5T27duH6dOnY/fu3fB0HQpXvzPaXXpDjfydeqFh8LmQrRmYO3cuXnzxRUiSZHRZuvB6vVi6dBlkawb8mV2NLqeRIMCbV4yG+nqsWrXK6GpSRrjBCYIA2ZLG4EREpIdUGQ7B4KQpDoeIwqZNmzBz5kzU1dXB3XMcPN1GxFWXad68eS1ef/Ptd8W4krZJ9jw0DD4P9u1f4e2330ZlZSXuuecemM3J9c9y1apVqK+vg7fb8Lj6dwIoHTBb2UYsXrwYJ598stHlpIRw9zgBgGS2oYrBiYhIe1p2nGK1aoNT9QzHjlOEvv/+e9x55wzU1TfAWXwqPN1Hxt2b4UQi2zLRMOQ8+DML8NVXX2HWrFlwOBxGl6WpL7/8EgDgzYufZXoqKT0PUloOvvvuO9TV1RldTkpwOBzKdEUxjA8ITFY4k+zngYgoLqRKcGLHSVPJ9dG+zhYuXIgnnngCkiDCMeDs4Ob6eDN9+vSWbzDHx/mDmjHb4Bj0a6TtWopVq1bhzjvvxOOPP47c3FyjK+uw0tJSLF/+Lfz2zpDscTgwRBDg6TIYYsmP+Oijj3D11VcbXVHSczqdkE2WsO4rixZ4vV74fL6k68QSERlKi6V6se7mcBy54dhxClN1dTWe/Oc/4RetaBg4OW5DU8ISzXD1PxOeLgOxbds2/Otf/zK6Ik385z//gSxL8HSPr+WcobxdBkI22/D+++/DzU+kdOd0OiGH020CIJvMwccQEZGGtOg4qcGJHaeUweAUpq+//hp+nw/uHqMhZXYxupzkJIhw9z4JsiUdixYtgtfrNbqiDqmqqsLnCxdCsmXD16m30eW0zmSBp8tgVFdX44svvjC6mqSnBKfwOk4I3I/BiYhIY4k4HCKac08xOGmKwSlMX3zxJSCI8MbROOmkJIjw5vdDbW0tVq5caXQ1HfL+++/D6/HA0224sqcljnm7DgVEE9599134/X6jy0lqTqczvP1NYMeJiEg37DhRFOL73Vyc2LVrF3bu3AFvThHQ3ghh6jBv/gAASOjuh8vlwkcffQTZkg5v5/5Gl9Mu2ZIOT+cBOHjwIFasWGF0OUnN5/NBFsP8r1cwAQDDLBGR1jgcgqLA4BSG4FS0zgMMriQ1SPZO8NvzsXLlyoQ9h83333+P+vp6eDoPDLu7YDRvwVAAjf/eSR+yLAOIbL9bsp7jjIjIMKkyHILjyDXF4NQOSZKwaNEiyJY0DoSIIW/nAfD7/ViyZInRpURl0aJFAABvfvx3m1RSei789s748ccfEzawJgJJlsMfFBK4nxK2iIhIM6m2VI9T9TTB4NQOSZLgcDggm2xxOxUtGckWZXR6Q0ODwZVErrq6Gj/99BP8GZ0hp+cYXU5EvJ37we/345tvvjG6lKQlR9Q9Uv7PYceJiEhj0QxaOFasl8FxqZ7hGJzaYTabMWHCBIiuGojOaqPLSRnmo3sBAKeccoqxhURhyZIl8Pv98Ob3M7qUiPny+gKCEOyYkbYaO0fhfQij3psdJyIijalBQouleonQcWJw0gSDUxgmTpwIADBX7TG2kFTh98FSU4JevXqjuLjY6Goi9vXXXwOCoISQBCNb0uHLLsTmzZtRWlpqdDlERET64HAIigKDUxhOOOEE2Gw2WI7uBfjJr+7MNSWA5MMZZ0w0uJLo7N69G/70vOByw0Tjyy4EAOzZww8KtCYIAkRRRGMvqZ37B/6/MZlMOlZFRJSCUmU4BIOTphicwpCenh5YrlfN5XoxoC7TO/30040tJAputxsulythQxMAyBblRYQDIvRhMpkgyOHuWZKCjyEiIg2lynAItUZJAnw+7WtKMQxOYVKX61kPbWDXSUei42hCL9OrqakBAMjmDvxHbDA5cK4y9fdC2jKZTEC4wYkdJyIi7cmytkv1EqHjBHCyngYYnMJ08sknY8iQIbAc3QVr6Rqjy0lKgrse9h1fQZD9uOGG6yEk4BRDtUsjJ/CJktXQx+CkD1EUw//wRWbHiYhIc6EBIlWGQ4Q+nqLG4BQmi8WC2bNno6ioCLZDG2A5vNnokpKLzwX79i8heBy47bbbcNpppxldUVSCHSdLIgcndpz0FE3HSdkXRUREmggNEMk+HMJsbjydDoNTh/HVOAK5ubl44oknkJeXh7T9K2E+ys3zmvD7YN++CKKrBldddRUuvfRSoyuKWrAz4PcaW0gHCJJSO9+s60MUTQh7OAS4VI+ISHPqYAhAmz1O8bxUTxA4IEJDfGcUoW7duuGJJ56APSMD6buXwVR7yOiSEpssIX3XNzA1HMGvf/1r3HjjjUZX1CGDBw+GyWSCqa7M6FKiptY+cuRIgytJTkrHKbKlegyxREQaUgOE1drYjYlGIizVC70/g1OH8dU4Cv369cOjjzwCs0mEfediiA0VRpeUmGQJaXu/g7mmBCeccALuvvvuhNzXFMput2Pw4MEwN1QkbNfJVKsEp9GjRxtbSJIymcTgmPF2cTgEEZH2tBgMEfr4eO44AbHvjCUxBqcojR49Gn/5y18gSF5kbP0c5oodRpeUUASvE+nbvoSlYgeGDBmCv/71rzCbzUaXpYnRo0cDsgRTfbnRpUROlmGuL0NBQQG6detmdDVJSQlB3ONERGQYLc7hBLDjlIKS452qQU4//XQ88sgjePTRR4E938JbVwZXrwmAiX+sbTHVHkL67qUQvE6cdtppuOeee5CenrjnPTrW6NGj8eabb8JUVwZ/TqFmx503b16L1998+12aPYfoqoHgdWLMmNMSvvsXr5SpeuHem8GJiEhzWnecEiU4cRx5h/HVuINOOukkLFiwAIMHD4alYgcytnwKwclpZC2SZVgP/gz7ti9glry47bbb8NBDDyEzM9PoyjQ1fPhwWKxWWI7uCX96WpwwH90NADjuuOMMriR5ybIMRJhJZZ47johIO1p3nOJ9qR47Tppha0QD3bp1w3PPPYcXX3wR7733HjK3fAJn75Pgy+9ndGlxQ/C6kLZnGcw1pSgoKMBf//pXDB061OiydJGeno7Jv/41PvnkE5ir9sGXp82JfKdPn97yDWaNunV+L6zlW5Cbmxs84TNpz+/3I+zkFOj6MTgREWlIq46TGpy8XmVptd4rNdhxMhw7ThqxWCz4wx/+gIceegh2mwXpu5fBtvd7QPIZXZrhxLrDyNj8Mcw1pZgwYQIWLFiQtKFJNWXKFAiCCOuhjeFPUDOY5ch2CD43LrvsMtg6+mJCrZIjenFV7qeELSIi0oTWS/UA/UOJJAE+X/PnDQeHQ2iGwUljp59+Ol5++WX0798f1iNbYd/yGUTH0Zg9v2xJg2ROh2ROhxx40yVDUH4d65OyShKsB39GxraFMPmcuOmmm/DII48gOzs7tnUYoLCwEBMnng6TowKmugQYWS9JsB3+BWnp6bj44ouNriap+f1S8GezXew4ERFpT+uleoD+wakjJ+2N9RCLJMbgpIPCwkI8//zzuPDCC2FyVCJj8yewlq4FJP0/NXYMvwQNY65Ew5grIdnzAACSPQ8NY66EY/gluj+/SmyogH3LJ7CVrkF+fh7mzJmDK6+8MqU2uV955ZUAoHSd4pz56G4IngZceMEFyMrKMrqcpCZJ/og7TpKUWHvliIjimtZL9YD4Dk5cqqeZ1HkXG2M2mw0zZszAk08+ia5dC2A7uB4Zmz+GmIgjqiMh+WAtWY2MLZ/C5DiKCy64AK+/9lpKnkx14MCBGDt2LMy1pTHtOkZMlmEt2wiTyYTLL7/c6GqSntfrBYTwzsski8r9PHyxIyLSjtpx6mhwMpmUL0D/ZXChxw8NbOHgUj3NMDjpbNy4cXj1lVdw2WWXweSqQcaW/8G2/8eEPTlqW0x1ZcjY9DFsZRvQo3t3PP3007jrrruSbmpeJKZMmQIAsJb9YnAlrTPVHoTJWYWzzjoLBQUFRpeT9FxudzAQtStwPzdf7IiItKP+n9rRpXpA7JbBqTVbrZEPoWDHSTMMTjFgt9tx22234bnnnkNRr16wHt6EjE0fwlRTanRp2vB7Ydv3PexbP4fJXYcpU6bglVdewZgxY4yuzHDHH388evfuDcvR3RA8DqPLaZH1sBLqfvOb3xhcSfLz+/3w+3yAGN5AUzlwPwYnIiINabVUL/QYseo4RVMzO06aYXCKoeHDh+P/FizA1VdfDYvPCfv2L2Hb8y3gS9x/yKbqEmT+8gGs5VtRXNwX8+fPwy233II0LT7FSQKCIOCKK64AZAmW8i1Gl9OM6KyCuaYUY8aMwYABA4wuJ+mpAUgOMziBwYmISHtaDYcAYt9x6khwYsepwxicYsxqteL666/Hiy++iIEDB8JasQOZmz6EqbrE6NIi43Mjbc+3sO9YBLPfjeuuuw4vvfQiBg8ebHRlcefss89GTk4urEe2Av74Gk9vKdsEgN2mWAnuVQpzqZ4scKkeEZHm9Og4xXNw4glwNcPgZJD+/ftj3rx5+P3vfw+r7IV9xyKkJUj3yVRzAJmbPoKlYgcGDRqMBQtextSpU2GxWIwuLS7ZbDZccsnFEHxumKv2GF1OI78X1qO70LNnT5x44olGV5MSnE4ngAg6Tiblfi7101EiIuo4rYZDALFbBseOU1xgcDKQ2WzGVVddhZdffhmDBg2GpWIHMjd9BFPNAaNLa5nPA9ueFbBv/woWyY0bb7wRzz8/F8XFxUZXFvcmTpwIADDXlRlbSAhTwxFA8mPixIkpNSbeSGpwghjehwxy4H7BxxERUccl8nCIjnScGJw6jO+W4kCfPn3w/PNzceONN8IsuWHf/hVse1YAvvj5B26qKUXmpg9hrdiOgQMH4qWXXsLvfvc7mM1hfnKe4nr16oWMzEyY6g8bXUqQqU6pZdiwYQZXkjqCHSdTmN3ZwP0cjvgcLEJElJA4HIKixOAUJ8xmM373u9/h5ZdewoABA2Ct2K7sfTJ68p7fC9ve72Df/mVwL9O8efPQt29fY+tKMKIoYsTw4RBdtRC88bHsyhQ4pxiDU+wEO0emMKfqmdhxIiLSHIdDUJQYnOJM3759MX/+fFx33XUw+93K5L293wFS7IcKmOrKlC7TkW3o378/XnrpRUydOpVdpiipASUuToIsSzA1HEHv3r2RnZ1tdDUpo3GPU7hL9cxNHkdERBrgcAiKEoNTHDKbzZg6dSpeeulF9O/fH9Yj22Df+nlMzwNkKd8K+7YvYPY5ce211+KFF15Av379Yvb8yWj48OEAGjs9RhJdNRD8HnabYizy4RDsOBERaU7L4MThECmFwSmO9evXD/Pnz8d5550HU0MFMrZ8CrGhUt8nlSXY9q9E2r7vkZuTjWeeeQbXXnstu0wa6NKlCwBA8Bv/iY8QmN6o1kSxERwrHu5SPY4jJyLSXqot1eNwCM0wOMU5i8WCu+++G7feeitErwMZWz+DuWqvPk/m9yB9x9ewHt6M4uK+eOGFF4JdEiLqOHWseKTjyBmciIg0xOEQFCUGpwQgCAJ+85vf4NFHH0WazYL0nUtgPfgzIMvaPYerFhlb/gdzzQFMmDABzz8/F926ddPs+EQUEoDCDE6ywOBERKS5VOs4cameZhicEsiECRMw7/nnUdC1K2yla5C2Zzkg+Tt8XFNdGTK3/g+isxpTpkzB3//+d9jtdg0qJqJQEXecRJ4Al4hIcxwOQVFicEowffv2xYsvvIBhw4bBUrkL6du+6NDEPVPVfti3fQGT5MM999yDW265BSaTScOKiUjlUV9YhTB/xkQREITGxxERUcdxOARFicEpAXXq1AlPP/00zjjjDJjrDyNt3w9RLdsTndWw71mGNJsN//znkzj33HN1qJZUXq9X+UYw/sdODtTg88V+zH0qC/55ixH8GxBE/j0REWkp1ZbqcTiEZox/B0dRsVqtmDVrFgYPHgxLxQ5YjmyL7AB+D9J3Lgb8XsyaNROjR4/WpU5q5HAo4+TVk5oaKlCDWhPFhhqA5EjCM4MTEZG2OByCosTglMCsVisefvhh5OTkIG3/yvBPrCrLSNv9LURXDa688kqcfvrp+hZKAELOxRPmyU/1pJ6AlcEptoIBKILgJDM4ERFpS+04ablUjx2nlMDglOAKCgrw17/+FQIA+65vIHjbP1GmtWwDLNX7cNxxx+H666/Xv0gCEF8dJ5knVjVENMGJHSciIo2pIUSLpXqJMByCHSfNMDglgTFjxuDmm2+C4GlA2q5vAElq9b6mmlLYDqxFQUEBHnjgAZ7YNobiKTiBHSdDsONERBQHOByCosTglCSuuOIKZVhEXRks5ZtavpPkQ/qe5bBYzHj44YeRm5sb0xopnijDRGQNzwVG7Yt2j1NwsAgREXUch0NQlBickoQgCLjrrruQlp4O2+EtgNy862Su3A3B68SUKVMwePBgA6pMbXl5eQAA0Wt8l0dd0pmfn29wJamlcbJi+CP/ZcEELztORETa8PsB9f9UDoegCDE4JZHMzExM/vWvIXjqYa7e3/RGWYa1fDNMJhMuuugiYwpMcWpIETzG7yticDJGMDhFMo5cFOH1sONERKSJ0PDA4RAUIQanJHPJJZcAACyHtzS53lR/GCbHUZx22mno0qWLEaWlvGBwioOOk9r1UrtgFBtKcBKiGA7B4EREpInQ4MThEBQhBqck06tXLxx//PEw1x0CpMblPZbDmwEAl112mVGlpbzs7GyYTKa4CE5qDew4xZbX642s24TAUj2vl/vRiIi0oIYHQQC0GJCVSMMhfL42B4hR++IiOM2bNw/FxcVIS0vD2LFj8e2337Z5f7fbjfvvvx+9e/eGzWZDv3798Morr8So2vinhiPBF9j8KEuwVO/DwIEDMWzYMAMrS22iKKKgoAAmV02Le9BiWouzGgDQtWtXQ+tINfX19ZBN1sgeZLLC7/fDpW5mJiKi6IUOhhCEjh8vkZbqAVyu10GGB6d3330Xd9xxB+6//36sW7cOp556KiZPnoz9+/e3+pgrrrgCixcvxv/93/9h27ZtePvttznsIMT48ePRtWtXCD7lh0PweQBZxoUXXghBi/8kKGrHH388BJ8bYv0R44qQZZhrSpCZmYVBgwYZV0cKqq2thWSK7EVPNiv3r6ur06MkIqLUouUo8tDjJELHCWBw6iDDg9NTTz2F66+/HjfccAOGDBmCOXPmoKioCPPnz2/x/l988QWWLVuGzz//HGeffTb69OmD8ePH46STTopx5fFLFEUMHz4cQmDktBBYsjdixAgjyyIg+O/UXF1iWA2isxqiux4nnngCz+MVQ7Iso66uLhiEwn5c4P41NTV6lEVElFq0Dk6J0HFicNKMocHJ4/FgzZo1mDRpUpPrJ02ahO+//77Fx3zyyScYN24c/vGPf6CwsBADBw7E3XffDaez9UllbrcbtbW1Tb6S3YABAxp/Iflgs9nQs2dP4woiAMrJim02G8w1rXdU9aZOXJwwYYJhNaQih8MBv98fdXBix4mISANansMJSIzhEKLYuJ+LAyI6xNDgVFFRAb/f32yfRdeuXVFWVtbiY3bv3o0VK1bgl19+wYcffog5c+bgvffew6233trq88yePRs5OTnBr6KiIk1/H/Gof//+we8F2Y/+/fvDZAr/3DGkD5vNhnHjxsHkrIbgMibAm6v3w2QyYfz48YY8f6pSP7Bhx4mIyEB6dZzieakeELvOWJIzfKkegGb7bmRZbnUvjiRJEAQBb775JsaPH49zzz0XTz31FF577bVWu06zZs1CTU1N8KukxLhlUrHSpOPUwq/JOCeffDIAwFK1N+bPLbjrYWo4glGjRiErKyvmz5/K1A+DZIs9osdJlgwAwOHDhzWviYgo5WjdcUqEpXqhj2PHqUOi2uCwYcOGsO87cuTIVm/r3LkzTCZTs+5SeXl5q9O+unfvjsLCQuTk5ASvGzJkCGRZxoEDB1oMCDabDTatPllIEDk5OTCbzfAFzo4d2oEiY5122ml45plnIB3ZBk+3EdpM9QmTpWI7AOCcc86J2XOSorS0FAAgpeW0c8+m5LRsAMCBAwc0r4mIKOWk4nAIgB0njUQVnEaPHt3udDa1a+T3+1u9j9VqxdixY7Fo0aLgiVsBYNGiRbjoootafMzJJ5+M//73v6ivr0dmZiYAYPv27RBFkXt4jmGxWILBqbCw0OBqSJWZmYmzzjoLn3/+OUy1B+HPidHfjSzBemQ7MjMzMXHixNg8JwWpne5Ig5NkywIgpESnnIhId4k4HEKWtes4MTh1SFRL9T744AMUFxdj3rx5WLduHdatW4d58+ahX79+eP/997F7927s2bMHu3fvbvdYM2bMwIIFC/DKK69gy5YtuPPOO7F//37cfPPNAJRldlOnTg3e/6qrrkJ+fj6mTZuGzZs3Y/ny5fjTn/6E6667Dunp6dH8dpJW6J6m7OxsAyuhY1144YUAAMuRbTF7TnN1CQSvA+ecc07KdWDjgdoxktIi/FkUTZBsmSgpYceJiKjDEnE4hM+nhKfQ54tUrPZiJbmoOk6PPvoonn32WZx77rnB60aOHImioiL85S9/wZo1a8I+1pQpU1BZWYmHH34Yhw4dwvDhw/H555+jd+/eAIBDhw41OadTZmYmFi1ahNtuuw3jxo1Dfn4+rrjiCvz973+P5reS1ESxMRdzP0t8GTRoEPr3H4Cdu3bB7XVEvO8lGpYjWwE0hjaKrZKSEsjmNCDC4RCA0qU6evQAHA4H7Hb9/60QESWtRBwOEXpsLtUzVFTBaePGjSguLm52fXFxMTZv3hzx8aZPn47p06e3eNtrr73W7LrBgwdj0aJFET9PqgntOKnLGik+CIKACy+8AE899RQsFTvh6d76XkBNns9dD3NNKUaOHBn8UIJix+12o7S0FP70zlE9XkrLAWoOYM+ePRg2bJjG1RERpRC146R1cPJ6la6QHvuWtQhOHA6hiaiW6g0ZMgR///vf4VL/8UF5Y/D3v/8dQ4YM0aw46pjQ4MRljPHnrLPOgsVqhblyZ2MLXieWyl0AgMmTJ+v6PNSyXbt2we/3Q8qILjj5A4/bvn27lmUREaUeNThovVQP0K+bo9Ycej6mSLHjpImo/vRfeOEFXHDBBSgqKsKoUaMAAD///DMEQcD//vc/TQuk6IUu1WtvmAfFXkZGBk45+WR88803EB2VUb+pbpcsw1K5E1arDaeffro+z0FtUgOP354f1eOlwOMYnIiIOkivpXqAEkr02EOsRc0cDqGJqILT+PHjsWfPHvz73//G1q1bIcsypkyZgquuugoZGRla10hRYliKf5MmTcI333wDS+UuuHUKTqKjEqKrBqeedRb3xxhEDTzRhmMpLQcwWbBtW+yGiRARJSW9zuME6N9x6khw4nAITUTZ7wPsdjt+//vfa1kLUco5/vjjkZOTi+qju+EuOh4QtD8ntaViJwAlpJExtm3bBojmyCfqqQQBvvQ87N27F263m1MRiYiipXXHyWRSvvx+/UIJO05xI+p3af/6179wyimnoEePHti3bx8A4Omnn8bHH3+sWXFEyc5sNuPss8+C4HXCVHtQ+yeQJViq9qBTp04YO3as9sendnk8Huzduxc+e16HgrGU0RmSJIV1mgciImqF1sEJ0H//EDtOcSOqV/H58+djxowZmDx5MqqqqoInue3UqRPmzJmjZX3UAVyqlxjUfUfmau3P0yM2VELwOnHKKafAHO2GUuqQffv2KYMhotzfpPLb8wAogyaIiChKWi/VA/SfWKdlcGLHqUOiCk7PPfccXn75Zdx///1N3oyNGzcOGzdu1Kw4olQwdOhQpKfbYa4t1fzY6jHHjx+v+bEpPDt3KkslpUDwiZb6ePV4REQUhVTtOHGpniaiCk579uzBmDFjml1vs9nQ0NDQ4aKIUonZbMZxx42B6KqB4K7X9NimmlKIoojRo0drelwKn9oh8qd3MDil5QKCyI4TEVFH6NlxiufgxKV6mogqOBUXF2P9+vXNrl+4cCGGDh3a0ZpII5IkGV0Chen4448HAJi13Ofk98DccARDhgxBVlaWdseliCgdIgGSvVPHDiSa4E/Lwc6du/izTUQULT07TvG8VI8dJ01EtenhT3/6E2699Va4XC7IsoyffvoJb7/9NmbPno0FCxZoXSNFSdb5pKqknXHjxgEATDUH4O0yUJNjmmrLAFkKhjIyxu49e+BPywbEju8xk+x5cFbuwuHDh9G9e3cNqiMiSjF6BCd2nFJGVK/k06ZNg8/nwz333AOHw4GrrroKhYWFeOaZZ/Db3/5W6xopSgxOiaOwsBBduhSgvPowIMuABoM9zHVlANDislqKDYfDgdqaGsg5RZocT7IpncOysjIGJyKiaOixVC8R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H7B8/vz5LFu2zCKrBEHojJqaGgDKy8sttkToCsRyrfjggw86bH/MMcfw6aef0tbWljRbYyER10K3201dXV3a/U/G+t4eeeQR1q9fz/XXX59sE2Mmlvf24osvMn36dP7yl7/Qr18/Ro4cya9+9SuamppSYXLExPLeZs2axbZt21i0aBFKKXbt2sUzzzzD8ccfnwqTk0omfZ+YOKw2QEg81dXVuFwuevXqFbC8V69eVFVVWWSVIAjhUEpxxRVXcOihhzJ+/HirzRG6ALFcK6qqqoJu73Q6qa6upk+fPkmzN1oScS289dZbaWho4Pvf/34yTIyZWN7bunXruPrqq3n33XdxONL39i+W97Zhwwbee+898vPzef7556muruaiiy5i3759aZXnFMt7mzVrFo899hinn346zc3NOJ1OvvOd73DHHXekwuSkkknfJybiccpiDMMIeK2U6rBMEIT04JJLLuGLL77giSeesNoUoYsR7bUi2PbBlqcLsV4Ln3jiCW644QaefPJJevbsmSzz4iLS9+ZyuTjzzDO58cYbGTlyZKrMi4toPje3241hGDz22GMcdNBBHHfccSxcuJBHH3007bxOEN17W7VqFZdeeim///3vWb58Oa+++iobN27kwgsvTIWpSSfTvk/S95GDEDM9evTAbrd3eHqxe/fuDspeEATr+cUvfsGLL77I0qVL6d+/v9XmCF2EWK4VvXv3Drq9w+GgoqIiabbGQjzXwieffJJzzz2Xp59+mqOOOiqZZsZEtO+trq6OTz/9lBUrVnDJJZcAWmwopXA4HLz++uscccQRKbG9M2L53Pr06UO/fv0oLS31LhszZgxKKbZt28aIESOSanOkxPLebrnlFmbPns2vf/1rACZOnEhRURFz5szhj3/8Y1p6ZSIlk75PTMTjlIXk5uYybdo0Fi9eHLB88eLFzJo1yyKrBEFoj1KKSy65hOeee4633nqLIUOGWG2S0IWI5Voxc+bMDtu//vrrTJ8+nZycnKTZGguxXgufeOIJfvzjH/P444+nbR5JtO+tpKSEL7/8kpUrV3p/LrzwQkaNGsXKlSs5+OCDU2V6p8Tyuc2ePZsdO3ZQX1/vXbZ27VpsNltaPYyK5b01NjZiswXertvtdsDnnclUMun7xIsVFSmE5POf//xH5eTkqIceekitWrVKXXbZZaqoqEht2rTJatOEGKmrq1MrVqxQK1asUIBauHChWrFihdq8ebPVpgkx8vOf/1yVlpaqd955R+3cudP709jYaLVpQhehs2vF1Vdfrc4++2zv9hs2bFCFhYXq8ssvV6tWrVIPPfSQysnJUc8884xVbyEs0b6/xx9/XDkcDnXXXXcF/E8eOHDAqrcQkmjfW3vSuapetO+trq5O9e/fX5122mnq66+/VkuWLFEjRoxQ5513nlVvISTRvrdHHnlEORwOdffdd6v169er9957T02fPl0ddNBBVr2FkHR2n5Lp3ydKKSXCKYu566671KBBg1Rubq6aOnWqlDjOcN5++20FdPj50Y9+ZLVpQowE+zwB9cgjj1htmtCFCHet+NGPfqTmzp0bsP0777yjpkyZonJzc9XgwYPVPffck2KLoyOa9zd37tyM+p6N9rPzJ52Fk1LRv7fVq1ero446ShUUFKj+/furK664Im0fQkX73m6//XY1duxYVVBQoPr06aPOOusstW3bthRb3Tmd3adkw/eJoVSG+/kEQRAEQRAEQRCSjOQ4CYIgCIIgCIIgdIIIJ0EQBEEQBEEQhE4Q4SQIgiAIgiAIgtAJIpwEQRAEQRAEQRA6QYSTIAiCIAiCIAhCJ4hwEgRBEARBEARB6AQRToIgCIIgCIIgCJ0gwkkQBAAMw+CFF16w2gxBEIQuw7x587jsssusNiNj+OabbzjkkEPIz89n8uTJVpsjdEFEOAlCEvnxj3/MySefbLUZAdxwww1ywREEQRAyjuuvv56ioiLWrFnDm2++abU5QhdEhJMgpAFtbW1WmyAIgiB0YTLhOrR+/XoOPfRQBg0aREVFRdBtMuF9CJmLCCdBSADPPPMMEyZMoKCggIqKCo466ih+/etf849//IP//ve/GIaBYRi88847bNq0CcMweOqpp5g3bx75+fn8+9//BuCRRx5hzJgx5OfnM3r0aO6++27vOcz9nnvuOQ4//HAKCwuZNGkSH3zwQYAtDzzwAAMGDKCwsJBTTjmFhQsXUlZWBsCjjz7KjTfeyOeff+616dFHH/XuW11dzSmnnEJhYSEjRozgxRdfTPrvThAEQYD9+/dzzjnn0L17dwoLC1mwYAHr1q0DQClFZWUlzz77rHf7yZMn07NnT+/rDz74gJycHOrr6wGoqanhggsuoGfPnpSUlHDEEUfw+eefe7c3ow8efvhhhg4dSl5eHkopDhw4wAUXXECvXr3Iz89n/PjxvPzyywDs3buXM844g/79+1NYWMiECRN44oknAt5HsOthQ0ODd32461w4DMNg+fLl3HTTTRiGwQ033BDz9RTg448/ZsqUKeTn5zN9+nSef/55DMNg5cqVEdkjdFGUIAhxsWPHDuVwONTChQvVxo0b1RdffKHuuusuVVdXp77//e+rY489Vu3cuVPt3LlTtbS0qI0bNypADR48WD377LNqw4YNavv27er+++9Xffr08S579tlnVXl5uXr00UeVUsq73+jRo9XLL7+s1qxZo0477TQ1aNAg1dbWppRS6r333lM2m0399a9/VWvWrFF33XWXKi8vV6WlpUoppRobG9WVV16pxo0b57WpsbFRKaUUoPr3768ef/xxtW7dOnXppZeqbt26qb1791ryexUEQch25s6dq375y18qpZT6zne+o8aMGaOWLl2qVq5cqY455hg1fPhw1draqpRS6rvf/a665JJLlFJK7du3T+Xk5KiysjL19ddfK6WUuvnmm9XBBx+slFLK7Xar2bNnqxNPPFF98sknau3aterKK69UFRUV3u/066+/XhUVFaljjjlGffbZZ+rzzz9XTqdTHXLIIWrcuHHq9ddfV+vXr1cvvfSSWrRokVJKqW3btqm//vWvasWKFWr9+vXq9ttvV3a7XX344YdKqfDXQ6VUp9e5cOzcuVONGzdOXXnllWrnzp2qrq4u5utpfX29qqysVKeffrr66quv1EsvvaSGDh2qALVixYoEfLJCtiLCSRDiZPny5QpQmzZt6rDuRz/6kTrppJMClplf9LfddlvA8gEDBqjHH388YNkf/vAHNXPmzID9HnzwQe/6r7/+WgFq9erVSimlTj/9dHX88ccHHOOss87yCiel9MVy0qRJHWwF1HXXXed9XV9frwzDUK+88kroNy8IgiDEjCmc1q5dqwD1/vvve9dVV1ergoIC9dRTTymllLr99tvV+PHjlVJKvfDCC2r69Onqu9/9rrrrrruUUkrNnz9f/eY3v1FKKfXmm2+qkpIS1dzcHHC+YcOGqfvuu08ppa8FOTk5avfu3d71r732mrLZbGrNmjURv4fjjjtOXXnllUqp8NdDpTq/znXGpEmT1PXXX+99Hev19L777lPl5eWqoaHBu/6ee+4R4SR0ioTqCUKcTJo0iSOPPJIJEybwve99jwceeID9+/d3ut/06dO98z179rB161bOPfdcunXr5v354x//yPr16wP2mzhxonfep08fAHbv3g3AmjVrOOiggwK2b/86HP7HLioqori42HtsQRAEITmsXr0ah8PBwQcf7F1WUVHBqFGjWL16NaAr8H399ddUV1ezZMkS5s2bx7x581iyZAlOp5Nly5Yxd+5cAJYvX059fT0VFRUB15SNGzcGXFMGDRpEZWWl9/XKlSvp378/I0eODGqny+XiT3/6ExMnTvQe+/XXX2fLli1A+OthNNe5aIn2erp69WomTZpEYWGhd7+ZM2fGZYPQNXBYbYAgZDp2u53FixezbNkyXn/9de644w6uvfZaPvroo7D7FRUVeedutxvQ+Un+F07z+P7k5OR454ZhBOyvlPIuM1FKRfxe/I9tHt88tiAIgpAcQn1P+3+njx8/noqKCpYsWcKSJUu46aabGDBgAH/605/45JNPaGpq4tBDDwX0NaFPnz688847HY5p5rxC4HUIoKCgIKydt956K3//+9+57bbbmDBhAkVFRVx22WW0trYC4a+HpkiJ5DoXLdFeT6O5LgqCPyKcBCEBGIbB7NmzmT17Nr///e8ZNGgQzz//PLm5ubhcrk7379WrF/369WPDhg2cddZZMdsxevRoPv7444Bln376acDrSG0SBEEQUsPYsWNxOp189NFHzJo1C9CFGNauXcuYMWMAfZ057LDD+O9//8tXX33FnDlzKC4upq2tjXvvvZepU6dSXFwMwNSpU6mqqsLhcDB48OCI7Zg4cSLbtm1j7dq1Qb1O7777LieddBI//OEPAS1S1q1b57XRtDPY9fCKK65IyHWuMyK5no4dO5Z//etfNDU1ecXihx9+mDSbhOxBhJMgxMlHH33Em2++yfz58+nZsycfffQRe/bsYcyYMTQ3N/Paa6+xZs0aKioqKC0tDXmcG264gUsvvZSSkhIWLFhAS0sLn376Kfv37+eKK66IyJZf/OIXHHbYYSxcuJATTzyRt956i1deeSXACzV48GA2btzoDckoLi4mLy8v7t+DIAiCEBsjRozgpJNO4vzzz+e+++6juLiYq6++mn79+nHSSSd5t5s3bx6XX345U6ZMoaSkBIDDDjuMxx57LOA6cdRRRzFz5kxOPvlk/vznPzNq1Ch27NjBokWLOPnkkwNC2/yZO3cuhx12GKeeeioLFy5k+PDhfPPNNxiGwbHHHsvw4cN59tlnWbZsGd27d2fhwoVUVVV5hVO46yEk5joXCZ2d58wzz+Taa6/l3HPP5brrrmPTpk387W9/S9j5hexFcpwEIU5KSkpYunQpxx13HCNHjuS6667j1ltvZcGCBZx//vmMGjWK6dOnU1lZyfvvvx/yOOeddx4PPvggjz76KBMmTGDu3Lk8+uijDBkyJGJbZs+ezb333svChQuZNGkSr776Kpdffjn5+fnebU499VSOPfZYDj/8cCorKzuUkhUEQRBSzyOPPMK0adM44YQTmDlzJkopFi1aFBBCffjhh+NyuZg3b5532dy5c3G5XN78JtBen0WLFnHYYYfx05/+lJEjR/KDH/yATZs20atXr7B2PPvss8yYMYMzzjiDsWPHctVVV3mjFH73u98xdepUjjnmGObNm0fv3r0DmryHux5CYq5zkdDZebp168ZLL73EqlWrmDJlCtdeey1//vOfE2qDkJ0YSgI9BSGrOf/88/nmm2949913rTZFEARBENKSTZs2MWTIEFasWMHkyZOtNkdIUyRUTxCyjL/97W8cffTRFBUV8corr/CPf/wj4gaDgiAIgiAIQnAkVE8QsoyPP/6Yo48+mgkTJnDvvfdy++23c95551ltliAIgiCE5Oabbw4oH+7/Y4b6CYLVSKieIAiCIAiCYCn79u1j3759QdcVFBTQr1+/FFskCB0R4SQIgiAIgiAIgtAJEqonCIIgCIIgCILQCSKcBEEQBEEQBEEQOkGEkyAIgiAIgiAIQieIcBIEQRAEQRAEQegEEU6CIAiCIAiCIAidIMJJEARBEARBEAShE0Q4CYIgCIIgCIIgdIIIJ0EQBEEQBEEQhE74/6Ep4tOYLvkKAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "get_dist(data, 'lowercase_freq')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "625d9982-5162-434a-af70-5db8fb1c2698",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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FdX5uBkzZigtLS1w6dq1a3MvFQAQI0aMGKGrr75ap512mi6++GL961//kiS98MILgfs4HI6gxxiGUWNbVVOnTtXBgwcDlx07djTP4sOI4AQgkhw6dEhr167V2rVrJZmH9Kxdu1bbt29vtueMquAk1b5zqm17VdG4gwIARKZWrVrptNNO07fffhuYruevPPkVFhbW+ENfVW63W6mpqUGXSEerHoBIsmrVKp155pk688wzJUlTpkzRmWeeqfvuu6/ZnjOqWvUyMjJq3TnFxcWpffv2dT7O7XbL7XY39/IAADZQVlamjRs3avDgwcrOzlZGRoZyc3MDO2+Px6O8vDw98sgjFq80vKg4AYgkQ4cODRRQWkpUVZwGDhyo3NzcoG1Lly5V//796zy+CQCA43HXXXcpLy9PW7du1RdffKFrrrlGxcXFuvHGG+VwODR58mQ9/PDDWrRokf773/9q/PjxSk5O1tixY61eeth4PNLRo8euE5wA2JGlFadDhw7pu+++C1z39ya2a9dO3bp109SpU7Vr1y69+OKLkqSJEydq9uzZmjJlin7+85/r888/17x58/Taa69Z9RIAADFu586duu6661RUVKSOHTvqnHPO0YoVK9S9e3dJ0j333KMjR45o0qRJ2r9/vwYMGKClS5cqJSXF4pWHT9Vqk0RwAmBPlganVatW6YILLghcnzJliiTpxhtv1IIFC5Sfnx90gFd2drYWL16sO++8U08//bSysrL01FNPMYocANBsXn/99Xpvdzgcmj59uqZPn94yC7JA9WG0nMcJgB1ZGpwa6k1csGBBjW1DhgzRl19+2YyrAgAAVVFxAoAoO8YJAAC0PIITABCcAABAA6q36hGcANgRwQkAANSLihMAEJwAAEADqDgBAMEJAAA0wOMJvk5wAmBHBCcAAFCv6kGJ4ATAjghOAACgXtXPHMJ5nABYacaMGfrJT36ilJQUderUSVdeeaU2b97c7M9LcAIAAPWi4gQgkuTl5enWW2/VihUrlJubq4qKCg0fPlyHDx9u1ue19AS4AAAg8hGcAESSJUuWBF2fP3++OnXqpNWrV+v8889vtuclOAEAgHpVb80jOAExyjAkb6k1z+1KlhyOkB56sPKcCe3atQvnimogOAEAgHpRcQJswlsq/a21Nc997SEprlWTH2YYhqZMmaLzzjtPffr0aYaFHUNw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jce43W653e7wLh6wGMMhYkP1oESrHiINJ8AFAJOlFaeEhAT169dPubm5Qdtzc3M1aNCgWh9z7rnnavfu3Tp06FBg2zfffCOn06kuXbo063qBSELFKTZUDU6GHFScEHGoOAGAyfJWvSlTpuj555/XX//6V23cuFF33nmntm/frokTJ0oy2+zGjRsXuP/YsWPVvn173XTTTdqwYYM+/vhj3X333frZz36mpKQkq14GAISEVj1EurqOcSI4AbAby8eRjxkzRnv37tWDDz6o/Px89enTR4sXL1b37t0lSfn5+dq+fXvg/q1bt1Zubq5uv/129e/fX+3bt9e1116rhx56yKqXAAAhC2rNczho1UPE8Re3GQ4BwO4sD06SNGnSJE2aNKnW2xYsWFBjW69evWq09wFANAoOSgQnRB5/ZcnfokerHgC7srxVDwDsjPM4IdIxjhwATAQnALBQ0DFNDoZDIPJUb9Wj4gTArghOAGCh6hWm8vJy+XhHighSvVWPihMAuyI4AYCFysrKZMh/Ti7zI1UnRBLGkQOAKaThEG3btm30yTf37dsXylMAgC14PB7znahhBN6RejweTtqNiFHXVD2CEwC7CSk4/e53v9NDDz2kSy65RAMHDpQkff7553r//ff1u9/9Tu3atQvrIgEgVtU2DIIBEYgktOoBgCmk4PTZZ5/pwQcf1G233RbYdscdd2j27Nn697//rXfeeSdc6wOAmFZWViZ/i54hhxwiOCGy0KoHAKaQjnF6//33demll9bYfskll+jf//73cS8KQMMa2y6LyGa26lVeqfyemmEKiAyMIwcAU0jBqX379lq0aFGN7e+8847at29/3IsC0DCDdy0xwVNermPJycRwCEQS/68aToALwO5CatV74IEHNGHCBC1btixwjNOKFSu0ZMkSPf/882FdIIDaUXGKfhUVFTJ8PsnpqtxybDgEECnqqjgRnADYTUjBafz48erdu7eeeuopvf322zIMQ6eccoo+++wzDRgwINxrBFALKk7RLxCQgqeRE5wQUWjVAwBTSMFJkgYMGKBXXnklnGsBAFs51pLHeZwQuWjVAwBTyCfA3bJli377299q7NixKiwslCQtWbJE69evD9viACCW1RWQCE6RZe7cuTr99NOVmpqq1NRUDRw4UO+9917gdsMwNH36dGVlZSkpKUlDhw6NqX0hFScA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HT16VPn5+UGByl+5KigokO/QnhqPMeLcgZPvyhnif8+qlaRajjeSpDZt2qjLSacEBSP/x7S0NCbftaBAcKpsf+T/FSxTS3BqqFUvIUE6fNgcyKfkZDM4MVkPQIwiOEWQHj166Fe/+pVuvvlm/fOf/9TbixZp7571StizQeVtusmT0afmiUWbg7dc8YWb5C7cKIfnkBwOhwade66uueYanXHGGbypbqTExERlZ2crOzu7xm0VFRXas2dPjUC1e/du87iqw7Wfk6yxHE6nOnXsqM6dT65ROcrKylJycvJxfX2Ej7/C5Kig4gSLVQlOjW3V8/+4Hj0qs+IkUXECELMIThEoLS1N119/vcaMGaO8vDy98cYb2rRpk+IPbFN52x4q69JfRmIz9I8bPsUVfafEXavlKD+ixKQkXXb11Ro9erS6dOkS/uezsbi4uED7W3X+46oq/O9cmsjhcKhNmzZMZ4sS1StOfN9gmVqGQzQUnIKyUjInwQUQ2whOESyucrz3RRddpP/+97969tlntW7dOsUf2K6y9FPlyeorucLzJstVnC/3jv/IVbpX7sREXX/Dz3TVVVepdevWYfn6aDz/cVWwh2MVp6NB14EWV2U4RGNb9ag4AbATglOU6NOnj5588knl5eVp7l/+oj0FXyth73cq63yWOUQixCl8jqPFcu9cqfj92+RwODRi5EhNmDCBN+5AC0mqfLPpKDffbNJGCcscb6seFScAMY7gFEUcDoeGDh2qgQMH6s0339RLL78sxw+fKb5wo8q6DpA3NbPxX8zrUcLur+Tes14yfDr99NN12223RfVIcSAaBYKTryLoOtDiQpiqF1RkouIEIMYRnKKQ2+3W9ddfr0svvVTz5s3Te++9J9fm91TeppvKup5d//FPhk/xRd/KvetLOcqPKD0jQ5N+8Qudf/75DH0ALFA9KBGcYJkQpupRcQJgJwSnKNa+fXvdc889Gj16tGbPnq2vvvpK8Qd3ypuYVudjHF6PnJ7DSkxK0rib/k9XX301448BC1U/pongBMtUGQ5RUXkmAypOAHAMwSkG5OTkaNasWfrkk080f/4C7d23t877Oh3xOnfYZfrZz37GcUxABIiPj1dcXFxgiiLDIWCZqsMhis1POcYJAI4hOMUIh8Oh888/X+eff77VSwHQRImJSTp0yPxrPxUnWCZcrXpUnADEqNBG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99579cknnyguLrLfFoby+r7//nt9+umnSkxM1KJFi1RUVKRJkyZp3759EXmcUyivcdCgQXrllVc0ZswYHT16VBUVFbr88sv15z//uSWW3Owi6XcNFacY5nA4gq4bhlFjG4DIcNttt2ndunV67bXXrF4KbKyp+43a7l/b9kgS6r7xtdde0/Tp07Vw4UJ16tSpuZYXFo19jV6vV2PHjtUDDzygnj17ttTyjltTvoc+n08Oh0OvvPKKzj77bI0cOVIzZ87UggULIrbqJDXtNW7YsEF33HGH7rvvPq1evVpLlizR1q1bNXHixJZYaouIlN81kf2nBYSkQ4cOcrlcNf4yUVhYWCOxA7De7bffrnfffVcff/yxunTpYvVyYEOh7DcyMjJqvX9cXJzat2/fbGsN1fHsGxcuXKgJEybojTfe0MUXX9ycyzwuTX2NJSUlWrVqldasWaPbbrtNkhk0DMNQXFycli5dqgsvvLBF1t4YoXwPMzMz1blzZ6WlpQW29e7dW4ZhaOfOncrJyWnWNTdVKK9xxowZOvfcc3X33XdLkk4//XS1atVKgwcP1kMPPRRx1d+miqTfNVScYlBCQoL69eun3NzcoO25ubkaNGiQRasCUJ1hGLrtttv09ttv68MPP1R2drbVS4JNhbLfGDhwYI37L126VP3791d8fHyzrTVUoe4bX3vtNY0fP16vvvpqxB8z0tTXmJqaqq+//lpr164NXCZOnKiTTz5Za9eu1YABA1pq6Y0Syvfw3HPP1e7du3Xo0KHAtm+++UZOpzMi/1AVymssLS2V0xn8lt7lckk6VpmJZhH1u6bFx1GgRbz++utGfHy8MW/ePGPDhg3G5MmTjVatWhk//PCD1UtDiEpKSow1a9YYa9asMSQZM2fONNasWWNs27bN6qUhRL/4xS+MtLQ0Y9myZUZ+fn7gUlpaavXSYEMN7Tfuvfde44Ybbgjc//vvvzeSk5ONO++809iwYYMxb948Iz4+3njzzTetegkNauprfPXVV424uDjj6aefDvo/euDAAateQoOa+hqri/Spek19fSUlJUaXLl2Ma665xli/fr2Rl5dn5OTkGDfffLNVL6FBTX2N8+fPN+Li4ow5c+YYW7ZsMT799FOjf//+xtlnn23VS6hXQ+9nIvl3DcEphj399NNG9+7djYSEBOOss85ixHGU++ijjwxJNS433nij1UtDiGr7fkoy5s+fb/XSYFP17TduvPFGY8iQIUH3X7ZsmXHmmWcaCQkJRo8ePYy5c+e28IqbrimvcciQIVH5e7ep38eqIj04GUbTX9/GjRuNiy++2EhKSjK6dOliTJkyJeL/QNXU1/jUU08Zp5xyipGUlGRkZmYa119/vbFz584WXnXjNPR+JpJ/1zgMIwZqeAAAAADQjDjGCQAAAAAaQHACAAAAgAYQnAAAAACgAQQnAAAAAGgAwQkAAAAAGkBwAgAAAIAGEJwAAAAAoAEEJwCSJIfDoXfeecfqZQAAUK933nlHJ510klwulyZPnmz1cmAjBCegGY0fP15XXnml1csIMn36dJ1xxhlWLwMAgJDccsstuuaaa7Rjxw79/ve/t3o5sJE4qxcAQCovL1d8fLzVywAA2JzH41FCQoLVy6jToUOHVFhYqEsuuURZWVm13sfr9crhcMjppD6A8OInCgiDN998U6eddpqSkpLUvn17XXzxxbr77rv1wgsv6O9//7scDoccDoeWLVumH374QQ6HQ3/72980dOhQJSYm6uWXX5YkzZ8/X71791ZiYqJ69eqlOXPmBJ7D/7i3335bF1xwgZKTk9W3b199/vnnQWt57rnn1LVrVyUnJ2v06NGaOXOm2rRpI0lasGCBHnjgAX311VeBNS1YsCDw2KKiIo0ePVrJycnKycnRu+++2+z/dgBgRz169NCsWbOCtp1xxhmaPn26JLN9eu7cuRoxYoSSkpKUnZ2tN954I3Bf/z7h9ddf16BBg5SYmKhTTz1Vy5YtC/qaGzZs0MiRI9W6dWulp6frhhtuUFFRUeD2oUOH6rbbbtOUKVPUoUMHDRs2TJK0fv16XXbZZUpNTVVKSooGDx6sLVu2SJJWrlypYcOGqUOHDkpLS9OQIUP05ZdfBj3v9OnT1a1bN7ndbmVlZemOO+4I3ObxeHTPPfeoc+fOatWqlQYMGFBj3bVZtmyZUlJSJEkXXnhhYL+6YMECtWnTRv/85z91yimnyO12a9u2bY16ngULFqhbt26BfeYTTzwR2GcCNRgAjsvu3buNuLg4Y+bMmcbWrVuNdevWGU8//bRRUlJiXHvttcall15q5OfnG/n5+UZZWZmxdetWQ5LRo0cP46233jK+//57Y9euXcazzz5rZGZmBra99dZbRrt27YwFCxYYhmEEHterVy/jn//8p7F582bjmmuuMbp3726Ul5cbhmEYn376qeF0Oo3HHnvM2Lx5s/H0008b7dq1M9LS0gzDMIzS0lLjV7/6lXHqqacG1lRaWmoYhmFIMrp06WK8+uqrxrfffmvccccdRuvWrY29e/da8u8KALGse/fuxp/+9KegbX379jXuv/9+wzDM38nt27c3nnvuOWPz5s3Gb3/7W8PlchkbNmwwDOPYPqFLly7Gm2++aWzYsMG4+eabjZSUFKOoqMgwDHP/1KFDB2Pq1KnGxo0bjS+//NIYNmyYccEFFwSec8iQIUbr1q2Nu+++29i0aZOxceNGY+fOnUa7du2Mq666yli5cqWxefNm469//auxadMmwzAM44MPPjBeeuklY8OGDcaGDRuMCRMmGOnp6UZxcbFhGIbxxhtvGKmpqcbixYuNbdu2GV988YXx7LPPBp5z7NixxqBBg4yPP/7Y+O6774zHHnvMcLvdxjfffFPvv1lZWZmxefNmQ5Lx1ltvBfar8+fPN+Lj441BgwYZn332mbFp0ybj0KFDDT7PihUrDIfDYcyYMcPYvHmz8eSTTxpt2rQJ7DOB6ghOwHFavXq1Icn44Ycfatx24403GldccUXQNv/ObtasWUHbu3btarz66qtB237/+98bAwcODHrc888/H7h9/fr1hiRj48aNhmEYxpgxY4zLLrss6Gtcf/31QTuB+++/3+jbt2+NtUoyfvvb3wauHzp0yHA4HMZ7771X94sHAISkMcFp4sSJQbcPGDDA+MUvfmEYxrF9wh//+MfA7eXl5UaXLl2MRx55xDAMw/jd735nDB8+POhr7Nixw5BkbN682TAMMzidccYZQfeZOnWqkZ2dbXg8nka9loqKCiMlJcX4xz/+YRiGYTzxxBNGz549a338d999ZzgcDmPXrl1B2y+66CJj6tSpDT7X/v37DUnGRx99FNg2f/58Q5Kxdu3aJj3PddddZ1x66aVBt48ZM4bghDrRqgccp759++qiiy7Saaedpp/+9Kd67rnntH///gYf179//8DnP/74o3bs2KEJEyaodevWgctDDz0UaI3wO/300wOfZ2ZmSpIKCwslSZs3b9bZZ58ddP/q1+tT9Wu3atVKKSkpga8NAGhZAwcOrHF948aNdd4nLi5O/fv3D9xn9erV+uijj4L2K7169ZKkoH1L1f2RJK1du1aDBw+u89jbwsJCTZw4UT179lRaWprS0tJ06NAhbd++XZL005/+VEeOHNEJJ5ygn//851q0aJEqKiokSV9++aUMw1DPnj2D1pWXl1djf9cUCQkJQfuwxjzPxo0ba/03BurCcAjgOLlcLuXm5mr58uVaunSp/vznP2vatGn64osv6n1cq1atAp/7fD5J5vFJAwYMqPH1q6q6I3M4HEGPNwwjsM3PMIxGv5bqO0mHwxH42gCA8HE6nTV+P5eXlzf4uOq/4+u7j8/n06hRo/TII4/UuI//D29S8P5IkpKSkur9+uPHj9ePP/6oWbNmqXv37nK73Ro4cKA8Ho8kqWvXrtq8ebNyc3P173//W5MmTdJjjz2mvLw8+Xw+uVwurV69usb+rXXr1g2+trokJSUF/ds05nmasn8EJIITEBYOh0Pnnnuuzj33XN13333q3r27Fi1apISEBHm93gYfn56ers6dO+v777/X9ddfH/I6evXqpf/85z9B21atWhV0vbFrAgA0n44dOyo/Pz9wvbi4WFu3bg26z4oVKzRu3Lig62eeeWaN+5x//vmSpIqKCq1evVq33XabJOmss87SW2+9pR49eigurvFv+U4//XS98MILdU58/eSTTzRnzhyNHDlSkrRjx46ggROSGWQuv/xyXX755br11lvVq1cvff311zrzzDPl9XpVWFiowYMHN3pNTdWY5znllFO0YsWKoG3VrwNVEZyA4/TFF1/ogw8+0PDhw9WpUyd98cUX+vHHH9W7d28dPXpU77//vjZv3qz27dsrLS2tzq8zffp03XHHHUpNTdWIESNUVlamVatWaf/+/ZoyZUqj1nL77bfr/PPP18yZMzVq1Ch9+OGHeu+994L+CtejRw9t3bpVa9euVZcuXZSSkiK3233c/w4AgMa78MILtWDBAo0aNUpt27bV7373uxqVkTfeeEP9+/fXeeedp1deeUX/+c9/NG/evKD7PP3008rJyVHv3r31pz/9Sfv379fPfvYzSdKtt96q5557Ttddd53uvvtudejQQd99951ef/11PffcczWez++2227Tn//8Z/2///f/NHXqVKWlpWnFihU6++yzdfLJJ+ukk07SSy+9pP79+6u4uFh33313UJVqwYIF8nq9GjBggJKTk/XSSy8pKSlJ3bt3V/v27XX99ddr3LhxeuKJJ3TmmWeqqKhIH374oU477bRAGDtePXv2bPB57rjjDg0aNEiPPvqorrzySi1dulRLliwJy/MjRll5gBUQCzZs2GBccsklRseOHQ2322307NnT+POf/2wYhmEUFhYaw4YNM1q3bh04mNV/QO+aNWtqfK1XXnnFOOOMM4yEhASjbdu2xvnnn2+8/fbbhmEYtT6utoNkn332WaNz585GUlKSceWVVxoPPfSQkZGREbj96NGjxtVXX220adPGkGTMnz/fMAzzQORFixYFrSctLS1wOwAgfA4ePGhce+21RmpqqtG1a1djwYIFNYZDPP3008awYcMMt9ttdO/e3XjttdcCj/fvE1599VVjwIABRkJCgtG7d2/jgw8+CHqeb775xhg9erTRpk0bIykpyejVq5cxefJkw+fzGYZhDof45S9/WWN9X331lTF8+HAjOTnZSElJMQYPHmxs2bLFMAzD+PLLL43+/fsbbrfbyMnJMd54442gYReLFi0yBgwYYKSmphqtWrUyzjnnHOPf//534Gt7PB7jvvvuM3r06GHEx8cbGRkZxujRo41169Y1+O9W13CI2gY6NOZ55s2bZ3Tp0sVISkoyRo0aZTz++OMMh0CdHIZBgycQy37+859r06ZN+uSTT6xeCgCgkRwOhxYtWqQrr7yy1tt/+OEHZWdna82aNTrjjDNadG2xbMGCBZo8ebIOHDhg9VIQgWjVA2LM448/rv/f3h3bMAgDARS9ns57MIYL78EsDEBFyxTswB7MQEuZIEU6pQlR8p7kys21XzrZtdboui7WdY1lWS4f6QIA8D7PkcOP2bYtaq3R933M8xzTNMUwDHePBQCp1trl+fDnM47j3ePx56zqAQDwFfZ9j+M4Xt6VUqKU8uGJ4EE4AQAAJKzqAQAAJIQTAABAQjgBAAAkhBMAAEBCOAEAACSEEwAAQEI4AQAAJIQTAABA4gTnaZIefYWAbgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "get_dist(data, 'uppercase_freq')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7542b33b-29d2-4aee-926b-7ccecf0c583d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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27YtWKEJQolIxkkQ/IDBYKBnz548+eSTrFmzBovFwty5c7FYLDgcjjK3T01NpXbt2uzcuZMmTZoU+WnYsKHbcbRo0YIVK1YUWbZy5coiv7sbkyAIglB+aNKkCVFRUSxfvrxg2cmTJ9m6dWux67do0YK9e/dy+PDhgmX//PNPqcfQne8CcQ0555xz2LBhAw0aNDjrOhgfH+/x+QlCIBDhJAg+8vfff/Pcc8+xcuVK9u7dy5w5czh69CgtW7akQYMGrFu3ji1btnDs2DFsNluJ+3niiSd4/vnnef3119m6dSvr16/no48+YvLkyW7Hctddd7FgwQImT57Mtm3beOedd/jhhx+KPFVs0KABu3btYu3atRw7dgyr1erT+QuCIAihJyEhgdtuu40HHniAX375hf/++48RI0ZgNBZ/qzdgwAAaN27MzTffzLp161i2bBmPPvooQImZqPr162MwGJg/fz5Hjx4lMzPTb/GPHTuWEydOcO2117JixQp27tzJwoULufXWW3E4HB6fnyAEAvm0CYKPJCYmsnTpUi6++GKaNWvGpEmTePXVVxk0aBC33347zZs3p3PnzqSkpLBs2bIS9zNy5Ejef/99pk+fTtu2benduzfTp0/3KOPUs2dP3n77bSZPnkz79u358ccfmTBhAjExMQXrXHnllVx00UX07duXlJQUZs6c6dP5C4IgCOHByy+/zPnnn8+ll15K//79Oe+88+jUqVOx65pMJubNm0dmZibnnnsuI0eOZNKkSQBFrhmFqV27Nk8++SQPPfQQqampjBs3zm+x16pVi2XLluFwOLjwwgtp06YN99xzD0lJSQXiyJPzE4RAYNA8LYoVBKFccfvtt7N582Z+//33UIciCIIghDHLli3jvPPOY/v27TRu3DjU4bhFnz596NChQ5HxqQQhUIg5hCBEGK+88goDBgwgPj6eH374gY8//rjIQLqCIAiCADB37lwSEhJo2rQp27dv55577qFnz57lRjQJQrAR4SQIEcaKFSt46aWXyMjIoFGjRkydOpWRI0eGOixBEAQhzMjIyGDixIns27eP5ORk+vfvz6uvvur29nv37qVVq1Ylvr5x40bq1avnj1AFISyQUj1BEARBEATBY+x2O7t37y7x9QYNGmA2yzN6IXIQ4SQIgiAIgiAIglAG4qonCIIgCIIgCIJQBiKcBEEQBEEQBEEQykCEkyAIgiAIgiAIQhmIcBIEQRAEQRAEQSgDEU6CIAiCIAiCIAhlIMJJEARBEARBEAShDEQ4CYIgCIIgCIIglIEIJ0EQBEEQBEEQhDL4f3WI/NyPDPOTAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "get_dist(data, 'digit_freq')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "8081cfe8-2820-4696-815c-ad82415a4453",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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XHON9u3bV+HjLHQGAAAAyisoKJBhGGrSpIlCQkJ8XY7XNGnSRPv371dBQYHXZyf4dBOOwMBAxcfHuy1MlqTk5OQLWphsGIZbB6uix7du3eq2QxUAAACAqqmLna/SzHx9Pt+GfuLEiRo2bJi6du2qhIQELVy4UOnp6Ro9erSkouugHDp0SG+++aYk6cUXX1SrVq3Url07SUXXBXv22Wc1btw41zmnT5+u7t27q23btsrJydHcuXO1detWvfjii+a/QAAAAAAo5vMANnToUB09elQzZsxQRkaG4uLitGLFCtfi5oyMDKWnp7vGO51OTZkyRWlpafL399ell16qp59+WqNGjXKNOX78uB544AFlZmYqMjJSXbp00dq1a3Xttdea/voAAAAAoIRPN+GoqVjoDAC+w8/givG+APCFM2fOKC0tTbGxsQoODvZ1ORds/vz5+uc//6mMjAxdeeWVmjNnjnr16lVu3Llep6d//vr8QswAAAAA4GnLli3ThAkTNHXqVKWmpqpXr14aOHCg2+w6XyCAAQAAAKhzZs2apREjRmjkyJFq37695syZo5YtW2rBggU+rcvna8AAAAAA1BKGIZ065ZvnDg2VqrhbYX5+vlJSUjR58mS34/3799eGDRu8UV2VEcAAAAAAVM2pU1K9er557txcKSysSkOPHDkih8NR7trCUVFR5a5BbDamIAIAAACok8pe38swDJ9f04wOGAAAAICqCQ0t6kT56rmrqHHjxvLz8yvX7crKyirXFTMbAQwAAABA1dhsVZ4G6EuBgYGKj49XcnKy7rjjDtfx5ORkDR482IeVEcAAAAAA1EETJ07UsGHD1LVrVyUkJGjhwoVKT0/X6NGjfVoXAQwAAABAnTN06FAdPXpUM2bMUEZGhuLi4rRixQrFxMT4tC4CGAAAAIA6acyYMRozZoyvy3DDLogAAAAAYBICGAAAAACYhAAGAAAAACYhgFncyZMn9fe//1179uzxdSkAAB85dcrXFQCAdRDALO7TTz/VunXr9PTTT/u6FACADzz1VNElfT76yNeVAIA1EMAs7vTp05Kk/fv3+7YQAIBPPPpo0X9HjfJtHQBgFQQwAAAgm83XFQCANRDAAACA7PxGAACm4MctAACgAwYAJiGAAQAAAhgAmIQAZnE2PnEBAGIKIoC6Z+3atbr11lvVvHlz2Ww2vf/++74u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atSokTdrAwAAXkTgAgDzXdAuiOHh4YqLi9OiRYvUs2dPBQUFnXP8kiVLdNttt5Xbph4AANQ8BDIA8L5qbWN4//33nzd8SdKoUaP0yy+/VOcpAACAl7EGDADM59V95A1+kgMAAACACxfyAgDAouiAAYD5CGAAAFgUAQwAzEcAAwAAAACTEMAAALAoOmAAYL4LDmAOh0Nr1qzRsWPHzjs2JiZGAQEB1SoMAACYiwAGAN53wQHMz89PAwYM0PHjx887dseOHWrZsmV16gIA4KKlpaX5uoQajcAFAOar1hTEjh076scff/R0LQAAeNRll12mG264QW+//bbOnDnj63JqPAIZAHhftQLYU089pUmTJum///2vMjIylJOT43YDAKAm2LZtm7p06aKHH35Y0dHRGjVqlL7++mtfl1VjsAYMAMxXrQB20003adu2bbrtttvUokULNWjQQA0aNFD9+vXVoEEDT9cIAEC1xMXFadasWTp06JAWLVqkzMxMXXfddbryyis1a9YsHT582NclAgAsxr863/Tll196ug4AALzG399fd9xxh26++WbNnz9fU6ZM0aRJkzRlyhQNHTpU//jHP9SsWTNfl2k6OmAAYL5qBbA+ffp4ug4AALxm8+bNev3117V06VKFhYVp0qRJGjFihH7++Wc99thjGjx4sCWnJhK4AMB81QpgJU6dOqX09HTl5+e7He/UqdNFFQUAgCfMmjVLixYt0t69e3XzzTfrzTff1M033yy7vWgGfmxsrF5++WW1a9fOx5XWDAQyAPC+agWww4cP649//KM++eSTCh93OBwXVRQAAJ6wYMEC/elPf9If//hHRUdHVzimVatWeu2110yurGZgCiIAmK9am3BMmDBBx44d06ZNmxQSEqJPP/1Ub7zxhtq2basPP/zQ0zUCAFAtycnJ+r//+79y4cswDKWnp0uSAgMDdf/99/uiPACABVWrA/bFF1/ogw8+0DXXXCO73a6YmBj169dPERERSkxM1KBBgzxdJ7zE4J87AdRhl156qTIyMtS0aVO347/++qtiY2MtP2ODDhgAmK9aHbCTJ0+6PswaNmzo2sa3Y8eO2rJli+eqAwDgIlT2j0y5ubkKDg42uZqajwAGAN5XrQ7YFVdcob1796p169a66qqr9PLLL6t169Z66aWXLLmNLwCgZpk4caIkyWaz6bHHHlNo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DTeUe+w3v/mNJk+erH/9618+qKxmIXABgPmqFcAcDofq1asnSWrcuLF+/vlnSUUbdezdu/eCzzd//nzFxsYqODhY8fHxWrduXaVjMzIydM899+iKK66Q3W7XhAkTyo1JSkqSzWYrdztz5swF1wYAqH22b9+um266qdLHBw4cqG3btplYUe1AIAMA76tWAIuLi3NdmLlbt2565pln9L///U8zZsxQmzZtLuhcy5Yt04QJEzR16lSlpqaqV69eGjhwoNLT0yscn5eXpyZNmmjq1Knq3LlzpeeNiIhQRkaG2y04OPiCagMA1E6//vqroqKiKn08KipKx44dM7GimokpiABgvmoFsEcffVROp1OS9OSTT+rAgQPq1auXVqxYoblz517QuWbNmqURI0Zo5MiRat++vebMmaOWLVtqwYIFFY5v3bq1nn/+ed13332KjIys9Lw2m03R0dFuNwCANTgcDvn7V77PlJ+fnwoLC02sCACAItXaBXHAgAGur9u0aaNdu3bp119/VYMGDS5oW9/8/HylpKRo8uTJbsf79++vDRs2VKc0l9zcXMXExMjhcOiqq67SE088oS5dulzUOesig3/uBFAHGYah4cOHKygoqMLH8/LyTK6oZqIDBgDmu6jrgJXWsGHDC/6eI0eOyOFwlJsmEhUVpczMzGrX0q5dOyUlJaljx47KycnR888/r549e2rbtm1q27ZtufF5eXluH8Y5OTnVfm4AgO/df//95x1z3333mVBJ7UIAAwDvq3IAu/POO5WUlKSIiAjdeeed5xz73nvvXVARZbtmF3uBzO7du6t79+6u+z179tTVV1+tefPmVThFMjExUdOnT6/28wEAapZFixb5uoRagcAFAOarcgCLjIx0haJzrb26EI0bN5afn1+5bldWVtY5F09fKLvdrmuuuUb79u2r8PEpU6Zo4sSJrvs5OTlq2bKlx54fAIDagEAGAN5X5QBW+l8TPfUvi4GBgYqPj1dycrLuuOMO1/Hk5GQNHjzYI88hFXXUtm7dqo4dO1b4eFBQUKXrBAAAqKtYAwYA5qvWGrC0tDQVFhaWW0+1b98+BQQEqHXr1lU+18SJEzVs2DB17dpVCQkJWrhwodLT0zV69GhJRd2pQ4cO6c0333R9z9atWyUVbbRx+PBhbd26VYGBgerQoYMkafr06erevbvatm2rnJwczZ07V1u3btWLL75YnZdbp5V0NS9myicAoHYicAGA+aoVwIYPH64//elP5QLYV199pVdffVWrV6+u8rmGDh2qo0ePasaMGcrIyFBcXJxWrFihmJgYSUUXXi57TbDSuxmmpKRo8eLFiomJ0f79+yVJx48f1wMPPKDMzExFRkaqS5cuWrt2ra699trqvFxLYDdEAAAfBQDgfdUKYKmpqerZs2e54927d9fYsWMv+HxjxozRmDFjKnwsKSmp3LHzhYXZs2dr9uzZF1yHldEBAwDrIXABgPmqdSFmm82mEydOlDuenZ0th8Nx0UUBAADzEcgAwPuqFcB69eqlxMREt7DlcDiUmJio6667zmPFAQAA72ETDgAwX7WmID7zzDPq3bu3rrjiCvXq1UuStG7dOuXk5OiLL77waIEAAAAAUFdUqwPWoUMHbd++XUOGDFFWVpZOnDih++67T3v27FFcXJyna4QJ2IQDAKzHMKSOLbdr2l2PKywolw4YAJigWh0wSWrevLlmzpzpyVrgQ2zCAQDWtP3pzpIkP7tDhvGkj6sBgLqvWh0wqWjK4b333qsePXro0KFDkqS33npL69ev91hxAADAe0p3vOJa7PBdIQBgIdUKYO+++64GDBigkJAQbdmyRXl5eZKkEydO0BUDAKCWKB3AjpxozBREADBBtQLYk08+qZdeekmvvPKKAgICXMd79OihLVu2eKw4AADgPcH+J11fH81tRAADABNUK4Dt3btXvXv3Lnc8IiJCx48fv9iaAACACUIDclxfFzqqvSwcAHABqhXAmjVrpu+//77c8fXr16tNmzYXXRTMxy6IAGA9/vZ819fBgWfogAGACaoVwEaNGqXx48frq6++ks1m088//6x//etfmjRpksaMGePpGuFFBC8AsC4/e4Hr65CA0wQwADBBteYbPPLII8rOztYNN9ygM2fOqHfv3goKCtKkSZM0duxYT9cIAAC8IKBUBywk8LQPKwEA66j2hO+nnnpKU6dO1a5du+R0OtWhQwfVq1fPk7UBAAAv8rOV6oAF0gEDADNc1Irb0NBQRUVFyWazEb4AAKhlAvxKrQELYA0YAJihWmvACgsL9fe//12RkZFq3bq1YmJiFBkZqUcffVQFBQXnPwEAAPC5sh0wAID3VasDNnbsWC1fvlzPPPOMEhISJEkbN27UtGnTdOTIEb300kseLRIAAHiev5/7GrBTdMAAwOuqFcCWLFmipUuXauDAga5jnTp1UqtWrfS73/2OAAYAQC3gX6oD5m8v9GElAGAd1ZqCGBwcrNatW5c73rp1awUGBl5sTQAAwASlrwPm71fIGjAAMEG1AtiDDz6oJ554Qnl5ea5jeXl5euqpp9iGHgCAWqL0FER/OwEMAMxQrSmIqamp+vzzz9WiRQt17txZkrRt2zbl5+frxhtv1J133uka+95773mmUgAA4FFuUxD9mIIIAGaoVgCrX7++7rrrLrdjLVu29EhBAADAHG4dMKYgAoApqhXA5s+fL6fTqbCwMEnS/v379f7776t9+/YaMGCARwuEd9lsNl+XAADwkbKbcBDAAMD7qrUGbPDgwXrrrbckScePH1f37t313HPP6fbbb9eCBQs8WiAAAPCOsh0wAID3VSuAbdmyRb169ZIkvfPOO4qKitKBAwf05ptvau7cuR4tEAAAeIe/nQ4YAJitWgHs1KlTCg8PlyStXLlSd955p+x2u7p3764DBw54tEAAAOAdAWxDDwCmq1YAu+yyy/T+++/r4MGD+uyzz9S/f39JUlZWliIiIjxaIAAAvpSYmKhrrrlG4eHhatq0qW6//Xbt3bvXbYxhGJo2bZqaN2+ukJAQXX/99dq5c6fbmLy8PI0bN06NGzdWWFiYbrvtNv30009mvpRy/OxciBkAzFatAPbYY49p0qRJat26tbp166aEhARJRd2wLl26eLRAAAB8ac2aNXrwwQe1adMmJScnq7CwUP3799fJkyddY5555hnNmjVLL7zwgr755htFR0erX79+OnHihGvMhAkTtHz5ci1dulTr169Xbm6ubrnlFjkcDl+8LEmS3Xb2uemAAYA5qrUL4t13363rrrtOGRkZruuASdKNN96oO+64w2PFAQDga59++qnb/UWLFqlp06ZKSUlR7969ZRiG5syZo6lTp7qug/nGG28oKipKixcv1qhRo5Sdna3XXntNb731lvr27StJevvtt9WyZUutWrXKZzsIE8AAwHzV6oBJUnR0tLp06SK7/ewprr32WrVr184jhQEAUBNlZ2dLkho2bChJSktLU2Zmpms6viQFBQWpT58+2rBhgyQpJSVFBQUFbmOaN2+uuLg415iy8vLylJOT43bzNLcAxhREADBFtQMYAABWYxiGJk6cqOuuu05xcXGSpMzM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7f1NS0tzvb+7d+9WQkKC23nK3gcqwiYcgAn8/PyUnJysDRs2aOXKlZo3b56mTp2qr7766pzfFxYW5vra6XRKKlq/1a1bt3LnL630B57NZnP7fsMwXMdKGBewC1bZD1ObzeY6NwCg6qr72VD65+7HH3+sSy65xO3xoKAgSVJISMgF1XPrrbeqZcuWeuWVV9S8eXM5nU7FxcW5rTurqqo897k+T06ePKn+/furf//+evvtt9WkSROlp6drwIAB5eop/VlZXWXP4XQ61axZM61evbrc2JI100B1EcAAk9hsNvXs2VM9e/bUY489ppiYGC1fvlyBgYFyOBzn/f6oqChdcskl+vHHH/WHP/yh2nW0a9dOX3/9tduxzZs3u92vak0AgItT2WeDJG3btk2nT592hZlNmzapXr16atGihRo0aKCgoCClp6erT58+FZ67U6dOeuONN6q0q9/Ro0e1e/duvfzyy+rVq5ckaf369dV+XRfy3BXZs2ePjhw5oqefflotW7aUVP6zypuuvvpqZWZmyt/fX61bt65wTPv27bVp0ybdd999rmObNm0yqULUZkxBBEzw1VdfaebMmdq8ebPS09P13nvv6fDhw2rfvr1at26t7du3a+/evTpy5IjbDlBlTZs2TYmJiXr++ef13Xff6dtvv9WiRYs0a9asKtcybtw4rVixQrNmzdK+ffv08ssv65NPPnHrirVu3VppaWnaunWrjhw5ory8vIt6/QCA8s712SBJ+fn5GjFihHbt2qVPPvlEjz/+uMaOHSu73a7w8HBNmjRJDz30kN544w398MMPSk1N1Ysvvqg33nhDkjR27Fjl5OTod7/7nTZv3qx9+/bprbfe0t69e8vV0qBBAzVq1EgLFy7U999/ry+++EITJ06s9mu7kOeuSKtWrRQYGKh58+bpxx9/1Icffqgnnnii2vVcqL59+yohIUG33367PvvsM+3fv18bNmzQo48+6gqC48eP1+uvv67XX39d3333nR5//HHt3LnTtBpRexHAABNERERo7dq1uvnmm3X55Zfr0Ucf1XPPPaeBAwfqz3/+s6644gp17dpVTZo00f/+979KzzNy5Ei9+uqrrq10+/Tpo6SkJNc8/aro2bOnXnrpJc2aNUudO3fWp59+qoceekjBwcGuMXfddZduuukm3XDDDWrSpImWLFlyUa8fAFDeuT4bJOnGG29U27Zt1bt3bw0ZMkS33nqrpk2b5vr+J554Qo899pgSExPVvn17DRgwQB999JHrM6FRo0b64osvlJubqz59+ig+Pl6vvPJKhR0pu92upUuXKiUlRXFxcXrooYf0z3/+s9qv7UKeuyJNmjRRUlKS/vOf/6hDhw56+umn9eyzz1a7ngtls9m0YsUK9e7dW3/60590+eWX63e/+53279+vqKgoSdLQoUP12GOP6f/+7/8UHx+vAwcO6C9/+YtpNaL2shkXsvgDQJ305z//WXv27Dnn9VMAAOYZPny4jh8/rvfff9/XpeACTJs2Te+//762bt3q61JQg7EGDLCgZ599Vv369VNYWJg++eQTvfHGG24XdAYAAIB3MAURsKCvv/5a/fr1U8eOHfXSSy9p7ty5GjlypK/LAgDUEqNHj3bbnr30bfTo0T6r68orr6y0rn/9618+qwsojSmIAAAAuCBZWVnKycmp8LGIiAg1bdrU5IqKHDhwoNLNrKKiohQeHm5yRUB5BDAAAAAAMAlTEAEAAADAJAQwAAAAADAJAQwAAAAATEIAAwAAAACTEMAAAAAAwCQEMAAAAAAwCQEMAAAAAExCAAMAAAAAk/x/p5qSTMew/FwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "get_dist(data, 'special_char_freq')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cffdd745-7876-4295-82ea-e043829cf2cc",
   "metadata": {},
   "source": [
    "## Applying TF_IDF on data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "2ae429a0-60ae-4c75-96d8-533564e717bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe = data.sample(frac=1)      # to shuffle the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "7ed7f8ff-0299-4c63-88ad-c1707fbb346f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>password</th>\n",
       "      <th>strength</th>\n",
       "      <th>length</th>\n",
       "      <th>lowercase_freq</th>\n",
       "      <th>uppercase_freq</th>\n",
       "      <th>digit_freq</th>\n",
       "      <th>special_char_freq</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>71240</th>\n",
       "      <td>h1c8h24q</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>0.50</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.50</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93210</th>\n",
       "      <td>vqtoan1010</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>0.60</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.40</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67525</th>\n",
       "      <td>megaw166</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>0.62</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.38</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7070</th>\n",
       "      <td>hardhammer8</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>0.91</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.09</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32348</th>\n",
       "      <td>nosaints10</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>0.80</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.20</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53168</th>\n",
       "      <td>dsaTvyTM2OQmyxDN</td>\n",
       "      <td>2</td>\n",
       "      <td>16</td>\n",
       "      <td>0.50</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.06</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19072</th>\n",
       "      <td>j3qq4h7h2w</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>0.60</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.40</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76681</th>\n",
       "      <td>jas666</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>0.50</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.50</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27646</th>\n",
       "      <td>ggbb112233</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>0.40</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.60</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27331</th>\n",
       "      <td>kinni1983</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "      <td>0.56</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100000 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               password  strength  length  lowercase_freq  uppercase_freq  \\\n",
       "71240          h1c8h24q         1       8            0.50            0.00   \n",
       "93210        vqtoan1010         1      10            0.60            0.00   \n",
       "67525          megaw166         1       8            0.62            0.00   \n",
       "7070        hardhammer8         1      11            0.91            0.00   \n",
       "32348        nosaints10         1      10            0.80            0.00   \n",
       "...                 ...       ...     ...             ...             ...   \n",
       "53168  dsaTvyTM2OQmyxDN         2      16            0.50            0.44   \n",
       "19072        j3qq4h7h2w         1      10            0.60            0.00   \n",
       "76681            jas666         0       6            0.50            0.00   \n",
       "27646        ggbb112233         1      10            0.40            0.00   \n",
       "27331         kinni1983         1       9            0.56            0.00   \n",
       "\n",
       "       digit_freq  special_char_freq  \n",
       "71240        0.50                0.0  \n",
       "93210        0.40                0.0  \n",
       "67525        0.38                0.0  \n",
       "7070         0.09                0.0  \n",
       "32348        0.20                0.0  \n",
       "...           ...                ...  \n",
       "53168        0.06                0.0  \n",
       "19072        0.40                0.0  \n",
       "76681        0.50                0.0  \n",
       "27646        0.60                0.0  \n",
       "27331        0.44                0.0  \n",
       "\n",
       "[100000 rows x 7 columns]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1cf488c7-079d-411b-9ad0-b549ce0087f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = list(dataframe['password'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "7f83a5af-521b-4dff-9cb4-edf3c70eeff5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "a1174c7a-70d8-4e6f-9748-d8209be40e48",
   "metadata": {},
   "outputs": [],
   "source": [
    "vectorizer = TfidfVectorizer(analyzer=\"char\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e54f6081-e45c-4164-9567-7458fc5d3dd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = vectorizer.fit_transform(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f66b81d2-464e-4bc1-83c1-2579d7604966",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100000, 99)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "b6dca78d-70c2-4338-95f0-b987fe9399ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.]])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "7dbe5a2f-3833-4fd6-855b-b27c17ce20e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.21420018, 0.24781923, 0.        , 0.3064636 ,\n",
       "       0.        , 0.        , 0.        , 0.31357401, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.32310378,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.66587726,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.39072591, 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "       0.        , 0.        , 0.        , 0.        ])"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.toarray()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "825bbe84-2efb-4568-b907-a6586cddcb17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['\\x04', '\\x06', '\\x08', '\\x0e', '\\x10', '\\x11', '\\x17', ' ', '!',\n",
       "       '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', '0', '1',\n",
       "       '2', '3', '4', '5', '6', '7', '8', '9', ';', '<', '=', '>', '?',\n",
       "       '@', '[', '\\\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f',\n",
       "       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\n",
       "       't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '¡', '¨',\n",
       "       '°', '±', '³', '´', 'µ', '·', 'ß', 'à', 'á', 'ä', 'æ', 'ç', 'é',\n",
       "       'ê', 'í', 'ñ', 'ó', 'õ', 'ö', '÷', 'ú', 'ü', 'ý', 'þ', '›'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vectorizer.get_feature_names_out()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "7a000c52-933d-4d06-9cd4-bcdb9621c169",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(vectorizer.get_feature_names_out())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "99054c7e-5b8c-4e76-b646-8d28071f6ed9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>\u0004</th>\n",
       "      <th>\u0006</th>\n",
       "      <th>\b</th>\n",
       "      <th>\u000e</th>\n",
       "      <th>\u0010</th>\n",
       "      <th>\u0011</th>\n",
       "      <th>\u0017</th>\n",
       "      <th></th>\n",
       "      <th>!</th>\n",
       "      <th>#</th>\n",
       "      <th>...</th>\n",
       "      <th>ñ</th>\n",
       "      <th>ó</th>\n",
       "      <th>õ</th>\n",
       "      <th>ö</th>\n",
       "      <th>÷</th>\n",
       "      <th>ú</th>\n",
       "      <th>ü</th>\n",
       "      <th>ý</th>\n",
       "      <th>þ</th>\n",
       "      <th>›</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99995</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99996</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99997</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99998</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99999</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100000 rows × 99 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         \u0004    \u0006    \b    \u000e    \u0010    \u0011    \u0017         !    #  ...    ñ    ó    õ  \\\n",
       "0      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "1      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "2      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "3      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "4      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "...    ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...   \n",
       "99995  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99996  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99997  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99998  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99999  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "\n",
       "         ö    ÷    ú    ü    ý    þ    ›  \n",
       "0      0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "1      0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "2      0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "3      0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "4      0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "...    ...  ...  ...  ...  ...  ...  ...  \n",
       "99995  0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "99996  0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "99997  0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "99998  0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "99999  0.0  0.0  0.0  0.0  0.0  0.0  0.0  \n",
       "\n",
       "[100000 rows x 99 columns]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names_out())\n",
    "df2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ba8a319-40a8-4123-9362-3fc6fd855a1d",
   "metadata": {},
   "source": [
    "## Apply ML Algorithm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "96e834dc-006f-4673-b4f0-7d09c20d8b99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>\u0004</th>\n",
       "      <th>\u0006</th>\n",
       "      <th>\b</th>\n",
       "      <th>\u000e</th>\n",
       "      <th>\u0010</th>\n",
       "      <th>\u0011</th>\n",
       "      <th>\u0017</th>\n",
       "      <th></th>\n",
       "      <th>!</th>\n",
       "      <th>#</th>\n",
       "      <th>...</th>\n",
       "      <th>õ</th>\n",
       "      <th>ö</th>\n",
       "      <th>÷</th>\n",
       "      <th>ú</th>\n",
       "      <th>ü</th>\n",
       "      <th>ý</th>\n",
       "      <th>þ</th>\n",
       "      <th>›</th>\n",
       "      <th>length</th>\n",
       "      <th>lowercase_freq</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>0.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>12</td>\n",
       "      <td>0.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>0.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>23</td>\n",
       "      <td>0.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8</td>\n",
       "      <td>0.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99995</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10</td>\n",
       "      <td>0.70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99996</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10</td>\n",
       "      <td>0.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99997</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>0.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99998</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>9</td>\n",
       "      <td>0.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99999</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11</td>\n",
       "      <td>0.73</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100000 rows × 101 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         \u0004    \u0006    \b    \u000e    \u0010    \u0011    \u0017         !    #  ...    õ    ö    ÷  \\\n",
       "0      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "1      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "2      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "3      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "4      0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "...    ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...   \n",
       "99995  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99996  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99997  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99998  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "99999  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  ...  0.0  0.0  0.0   \n",
       "\n",
       "         ú    ü    ý    þ    ›  length  lowercase_freq  \n",
       "0      0.0  0.0  0.0  0.0  0.0       9            0.33  \n",
       "1      0.0  0.0  0.0  0.0  0.0      12            0.42  \n",
       "2      0.0  0.0  0.0  0.0  0.0       9            0.78  \n",
       "3      0.0  0.0  0.0  0.0  0.0      23            0.78  \n",
       "4      0.0  0.0  0.0  0.0  0.0       8            0.62  \n",
       "...    ...  ...  ...  ...  ...     ...             ...  \n",
       "99995  0.0  0.0  0.0  0.0  0.0      10            0.70  \n",
       "99996  0.0  0.0  0.0  0.0  0.0      10            0.80  \n",
       "99997  0.0  0.0  0.0  0.0  0.0       9            0.78  \n",
       "99998  0.0  0.0  0.0  0.0  0.0       9            0.67  \n",
       "99999  0.0  0.0  0.0  0.0  0.0      11            0.73  \n",
       "\n",
       "[100000 rows x 101 columns]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[\"length\"] = dataframe[\"length\"]\n",
    "df2[\"lowercase_freq\"] = dataframe[\"lowercase_freq\"]\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "00a0f184-9d7e-468b-9ba8-ce68755903c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = dataframe[\"strength\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "896cbda3-67b2-465d-af45-ec196ad3a55d",
   "metadata": {},
   "source": [
    "### Split data for Training and Testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "b4c4f64c-a83f-453a-ac69-87c4ccd3b1c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d5eafccd-b0c9-4640-a3a2-ef0249ca29d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(df2, y, train_size=0.8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "8ea05644-f17c-494d-b43e-af8ce23e96c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(80000, 101)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "778b1bb7-68c4-47ad-aa37-2ac623538818",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "9a789e55-7ceb-40fb-ad71-312c18907783",
   "metadata": {},
   "outputs": [],
   "source": [
    "reg = LogisticRegression(multi_class = \"multinomial\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "58a7dd74-a7af-48dd-9046-db9ebc5835a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-1 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-1 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-1 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-1 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-1 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(multi_class=&#x27;multinomial&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;&nbsp;LogisticRegression<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LogisticRegression.html\">?<span>Documentation for LogisticRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>LogisticRegression(multi_class=&#x27;multinomial&#x27;)</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression(multi_class='multinomial')"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "2af1fb62-f4bd-4c73-b9d2-df5b6ab7138b",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predict = reg.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "2edec2f0-0d56-4a50-adec-aba916082a9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "0868cee4-efd3-4f78-ad0d-a86d8711f8ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({1: 16639, 2: 1973, 0: 1388})"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Counter(y_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "3ce43072-63f6-4ecb-8d34-2d280e3ef21a",
   "metadata": {},
   "outputs": [],
   "source": [
    "password = \"%@123abcdef\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "496de0c7-63a5-4f15-89dd-441f002702df",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_array = np.array([password])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "d29b3157-e795-4ef5-8241-f6d8594bac07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1,)"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sample_array.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "e18b6dd6-9b40-4ca9-99ec-18c9e8e106ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_matrix = vectorizer.transform(sample_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "ac3779fe-c9b4-433d-9cde-775b1321d6b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.68867705, 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.13740016, 0.15896533, 0.17804186, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.46687214, 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.13232129, 0.22182066, 0.20725712,\n",
       "        0.19930316, 0.15500858, 0.24184373, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        ]])"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sample_matrix.toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "ee407f61-6a74-4099-a61d-81a6474cdaa6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 99)"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sample_matrix.toarray().shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "b8d608ae-4b00-4980-90a4-762ad8eaa466",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "403da673-2662-4061-86aa-002cfc49cbc8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd', 'e', 'f']"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[char for char in password if char.islower()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "4818d5f3-76c4-42de-a88d-363b202321d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5454545454545454"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len([char for char in password if char.islower()])/len(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "c101975d-23ee-492d-bffb-03e6257457de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(101,)"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.append(sample_matrix.toarray(), (9,0.4444)).shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "8870c042-f6f8-4de3-acf5-fba371f87e31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.68867705, 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.13740016, 0.15896533, 0.17804186, 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.46687214, 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.13232129, 0.22182066, 0.20725712,\n",
       "        0.19930316, 0.15500858, 0.24184373, 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 0.        ,\n",
       "        0.        , 0.        , 0.        , 0.        , 9.        ,\n",
       "        0.4444    ]])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_matrix = np.append(sample_matrix.toarray(), (9,0.4444)).reshape(1,101)\n",
    "new_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "97eaffe1-b6bc-4448-b90c-acadd8a38622",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0], dtype=int64)"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.predict(new_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "8da75f1f-d757-488c-8dd5-e93f756ce68f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict():\n",
    "    password = input(\"Enter a password : \")\n",
    "    sample_array = np.array([password])\n",
    "    sample_matrix = vectorizer.transform(sample_array)\n",
    "    \n",
    "    length_password = len(password)\n",
    "    length_normalised_lowercase = len([char for char in password if char.islower()])/len(password)\n",
    "    \n",
    "    matrix = np.append(sample_matrix.toarray() , (length_password , length_normalised_lowercase)).reshape(1,101)\n",
    "    result = reg.predict(matrix)\n",
    "    \n",
    "    if result == 0 :\n",
    "        return \"Password is weak\"\n",
    "    elif result == 1 :\n",
    "        return \"Password is normal\"\n",
    "    elif result==2:\n",
    "        return \"password is strong\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "e502396a-dbc0-4377-9180-d00813f50c29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a password :  vectorizer\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Password is normal'"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "4e31cc30-d1e8-4115-8122-1083bb0686a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix, accuracy_score, classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "988f75f3-c1a5-4a8e-a5f8-cb2ed134d4f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.794"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "9ca22b44-88a9-4533-8dbe-0477e73e6a4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[  700,  2016,     8],\n",
       "       [  599, 13682,   467],\n",
       "       [   89,   941,  1498]], dtype=int64)"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "confusion_matrix(y_test,y_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "44303f99-6aba-4b53-881d-71a15681ce19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.50      0.26      0.34      2724\n",
      "           1       0.82      0.93      0.87     14748\n",
      "           2       0.76      0.59      0.67      2528\n",
      "\n",
      "    accuracy                           0.79     20000\n",
      "   macro avg       0.70      0.59      0.63     20000\n",
      "weighted avg       0.77      0.79      0.77     20000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,y_predict))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96bdafe1-7ace-4053-9d0f-62ba3cd1a175",
   "metadata": {},
   "source": [
    "# Saving the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "114a1796-0b77-40de-91f4-6d2e65165d16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "ffb01055-0b7a-48b4-80c3-8b8139eac80b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('model', 'wb') as file:\n",
    "    pickle.dump(reg,file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "579e7941-ef83-472d-b9b4-079dce6221c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('scaler', 'wb') as file:\n",
    "    pickle.dump(vectorizer,file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea20e9d7-7526-47f8-b822-35cdd129eb45",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
