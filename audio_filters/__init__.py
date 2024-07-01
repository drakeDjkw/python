{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7b39e681",
   "metadata": {
    "papermill": {
     "duration": 0.004861,
     "end_time": "2024-07-01T19:01:29.821704",
     "exception": false,
     "start_time": "2024-07-01T19:01:29.816843",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**[Machine Learning Course Home Page](https://www.kaggle.com/learn/machine-learning)**\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3d845f4",
   "metadata": {
    "papermill": {
     "duration": 0.00424,
     "end_time": "2024-07-01T19:01:29.830654",
     "exception": false,
     "start_time": "2024-07-01T19:01:29.826414",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "This exercise will test your ability to read a data file and understand statistics about the data.\n",
    "\n",
    "In later exercises, you will apply techniques to filter the data, build a machine learning model, and iteratively improve your model.\n",
    "\n",
    "The course examples use data from Melbourne. To ensure you can apply these techniques on your own, you will have to apply them to a new dataset (with house prices from Iowa).\n",
    "\n",
    "The exercises use a \"notebook\" coding environment.  In case you are unfamiliar with notebooks, we have a [90-second intro video](https://www.youtube.com/watch?v=4C2qMnaIKL4).\n",
    "\n",
    "# Exercises\n",
    "\n",
    "Run the following cell to set up code-checking, which will verify your work as you go."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c9969ea6",
   "metadata": {
    "collapsed": true,
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:29.841757Z",
     "iopub.status.busy": "2024-07-01T19:01:29.841296Z",
     "iopub.status.idle": "2024-07-01T19:01:30.979719Z",
     "shell.execute_reply": "2024-07-01T19:01:30.978155Z"
    },
    "jupyter": {
     "outputs_hidden": true
    },
    "papermill": {
     "duration": 1.14773,
     "end_time": "2024-07-01T19:01:30.982874",
     "exception": false,
     "start_time": "2024-07-01T19:01:29.835144",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup Complete\n"
     ]
    }
   ],
   "source": [
    "# Set up code checking\n",
    "from learntools.core import binder\n",
    "binder.bind(globals())\n",
    "from learntools.machine_learning.ex2 import *\n",
    "print(\"Setup Complete\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba763458",
   "metadata": {
    "papermill": {
     "duration": 0.004381,
     "end_time": "2024-07-01T19:01:30.991965",
     "exception": false,
     "start_time": "2024-07-01T19:01:30.987584",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Step 1: Loading Data\n",
    "Read the Iowa data file into a Pandas DataFrame called `home_data`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bcb9ea06",
   "metadata": {
    "collapsed": true,
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:31.003342Z",
     "iopub.status.busy": "2024-07-01T19:01:31.002682Z",
     "iopub.status.idle": "2024-07-01T19:01:31.014857Z",
     "shell.execute_reply": "2024-07-01T19:01:31.013668Z"
    },
    "jupyter": {
     "outputs_hidden": true
    },
    "papermill": {
     "duration": 0.020965,
     "end_time": "2024-07-01T19:01:31.017490",
     "exception": false,
     "start_time": "2024-07-01T19:01:30.996525",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 4, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"1_LoadHomeData\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#ccaa33\">Check:</span> When you've updated the starter code, `check()` will tell you whether your code is correct. You need to update the code that creates variable `home_data`"
      ],
      "text/plain": [
       "Check: When you've updated the starter code, `check()` will tell you whether your code is correct. You need to update the code that creates variable `home_data`"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Path of the file to read\n",
    "iowa_file_path = '../input/home-data-for-ml-course/train.csv'\n",
    "\n",
    "# Fill in the line below to read the file into a variable home_data\n",
    "home_data = ____\n",
    "\n",
    "# Call line below with no argument to check that you've loaded the data correctly\n",
    "step_1.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a6ae489f",
   "metadata": {
    "collapsed": true,
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:31.029295Z",
     "iopub.status.busy": "2024-07-01T19:01:31.028850Z",
     "iopub.status.idle": "2024-07-01T19:01:31.034030Z",
     "shell.execute_reply": "2024-07-01T19:01:31.032705Z"
    },
    "jupyter": {
     "outputs_hidden": true
    },
    "papermill": {
     "duration": 0.014142,
     "end_time": "2024-07-01T19:01:31.036663",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.022521",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Lines below will give you a hint or solution code\n",
    "#step_1.hint()\n",
    "#step_1.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8626929a",
   "metadata": {
    "papermill": {
     "duration": 0.005348,
     "end_time": "2024-07-01T19:01:31.047409",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.042061",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Step 2: Review The Data\n",
    "Use the command you learned to view summary statistics of the data. Then fill in variables to answer the following questions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "896e6ab2",
   "metadata": {
    "collapsed": true,
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:31.060206Z",
     "iopub.status.busy": "2024-07-01T19:01:31.059770Z",
     "iopub.status.idle": "2024-07-01T19:01:31.067214Z",
     "shell.execute_reply": "2024-07-01T19:01:31.066020Z"
    },
    "jupyter": {
     "outputs_hidden": true
    },
    "papermill": {
     "duration": 0.016933,
     "end_time": "2024-07-01T19:01:31.070191",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.053258",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [],
      "text/plain": [
       "<learntools.core.constants.PlaceholderValue at 0x7fba2007c610>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print summary statistics in next line\n",
    "____"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e1f59928",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:31.083656Z",
     "iopub.status.busy": "2024-07-01T19:01:31.083144Z",
     "iopub.status.idle": "2024-07-01T19:01:31.093345Z",
     "shell.execute_reply": "2024-07-01T19:01:31.092151Z"
    },
    "papermill": {
     "duration": 0.020545,
     "end_time": "2024-07-01T19:01:31.096159",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.075614",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 4, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"2_HomeDescription\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#ccaa33\">Check:</span> When you've updated the starter code, `check()` will tell you whether your code is correct. You need to update the code that creates variables `avg_lot_size`, `newest_home_age`"
      ],
      "text/plain": [
       "Check: When you've updated the starter code, `check()` will tell you whether your code is correct. You need to update the code that creates variables `avg_lot_size`, `newest_home_age`"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# What is the average lot size (rounded to nearest integer)?\n",
    "avg_lot_size = ____\n",
    "\n",
    "# As of today, how old is the newest home (current year - the date in which it was built)\n",
    "newest_home_age = ____\n",
    "\n",
    "# Checks your answers\n",
    "step_2.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a8e6bbb5",
   "metadata": {
    "collapsed": true,
    "execution": {
     "iopub.execute_input": "2024-07-01T19:01:31.109766Z",
     "iopub.status.busy": "2024-07-01T19:01:31.109302Z",
     "iopub.status.idle": "2024-07-01T19:01:31.115016Z",
     "shell.execute_reply": "2024-07-01T19:01:31.113328Z"
    },
    "jupyter": {
     "outputs_hidden": true
    },
    "papermill": {
     "duration": 0.01589,
     "end_time": "2024-07-01T19:01:31.118040",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.102150",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#step_2.hint()\n",
    "#step_2.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7bf42b71",
   "metadata": {
    "papermill": {
     "duration": 0.006093,
     "end_time": "2024-07-01T19:01:31.130578",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.124485",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Think About Your Data\n",
    "\n",
    "The newest house in your data isn't that new.  A few potential explanations for this:\n",
    "1. They haven't built new houses where this data was collected.\n",
    "1. The data was collected a long time ago. Houses built after the data publication wouldn't show up.\n",
    "\n",
    "If the reason is explanation #1 above, does that affect your trust in the model you build with this data? What about if it is reason #2?\n",
    "\n",
    "How could you dig into the data to see which explanation is more plausible?\n",
    "\n",
    "Check out this **[discussion thread](https://www.kaggle.com/learn-forum/60581)** to see what others think or to add your ideas.\n",
    "\n",
    "# Keep Going\n",
    "\n",
    "You are ready for **[Your First Machine Learning Model](https://www.kaggle.com/dansbecker/your-first-machine-learning-model).**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6015be19",
   "metadata": {
    "papermill": {
     "duration": 0.005846,
     "end_time": "2024-07-01T19:01:31.142752",
     "exception": false,
     "start_time": "2024-07-01T19:01:31.136906",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "---\n",
    "**[Machine Learning Course Home Page](https://www.kaggle.com/learn/machine-learning)**\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 2709,
     "sourceId": 38454,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 108980,
     "sourceId": 260251,
     "sourceType": "datasetVersion"
    }
   ],
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 5.197419,
   "end_time": "2024-07-01T19:01:31.671394",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-07-01T19:01:26.473975",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
