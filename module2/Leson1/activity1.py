# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.

# (Also clean the input so it becomes either 'Y' or 'N'.)

#Example:

#medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

#if medical_cause == 'Y':

# 2) If `medical_cause` is 'Y':

# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):

# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"

# c) Else:

# - Print "Not allowed"
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()
if medical_cause == 'Y':
    print("he is allowed to give exam")
else:
    atten=int(input("enter ur atten"))
    if atten>=75:
        print("he is allowed to give exam")
    else:
        print("he is not alowed to give exam")
