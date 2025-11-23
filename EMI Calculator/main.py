import matplotlib.pyplot as mp


def calculateEMI(P,R,T):
    Actual_amount_per_month = (P/T)
    Intrest_amount_per_month = (P*(R/100))
    Total_emi_amount_with_intrest = P + (Intrest_amount_per_month*T)
    EMI = Actual_amount_per_month + Intrest_amount_per_month
    return [EMI, Total_emi_amount_with_intrest,Actual_amount_per_month, Intrest_amount_per_month]


def plot(P,R,T):
    calculate = calculateEMI(P,R,T)
    sizes = [P, calculate[3]*T, calculate[0]]
    labels = [f'Principal Amount - {sizes[0]}', f'Interest Amount - {sizes[1]}',f'Actual Amount per Month With Interest - {sizes[2]}']
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    mp.style.use('dark_background')
    mp.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,wedgeprops={'linewidth': 1, 'edgecolor': 'black'},textprops={'fontsize': 8, 'color': 'grey', 'weight':'bold','style':'italic', 'family': 'serif',})
    mp.show()

plot(5000,1,10)