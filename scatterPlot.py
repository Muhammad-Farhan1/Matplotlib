import matplotlib.pyplot as plt


# First scatter: Job Scale vs Salary
job_scale = [16,18,17,10,20]
salary = [34000 , 42000 , 38000 , 15000, 45000]
plt.scatter(job_scale, salary , color='blue' , marker='o' , label='Salary')

# Second scatter: Age vs Experience
age = [32,34,32,20,40]
experience = [5,7,6,3,8]
plt.scatter(age, experience , color='brown' , marker='*', label='Age')
plt.xlabel('Job Scale / Age')
plt.ylabel('Salary / Experience')
plt.title('Job Scale vs Salary and Age vs Experience')

plt.legend()
plt.show()