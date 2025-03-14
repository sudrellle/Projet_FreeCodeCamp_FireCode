import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def calculate_demographic_data(print_data=True):
    df=pd.read_csv('adult.data.csv')
    ##Combien de personnes de chaque race sont représentées dans cet ensemble de données ?
    # Il doit s'agir d'une série Pandas avec les noms de race comme étiquettes d'index. ( racecolonne)
    race_count=df['race'].value_counts()
    ##2. Quel est l'âge moyen des hommes ?
    average_age_men=round(df[df['sex']=='Male']['age'].mean(),2)

    ##3. Quel est le pourcentage de personnes possédant un baccalauréat ?
    percentage_bachelors=round(len(df[df['education']=='Bachelors'])/len(df)*100,2)

    # 4. Filtres éducation supérieure/inférieure
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. Pourcentage riches par niveau d'éducation
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 
        1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 
        1
    )

    

    ##6. Quel est le nombre minimum d’heures qu’une personne travaille par semaine ?
    heure_minimal=df['hours-per-week'].min()
    print("l'heure minimal par semaine est:",heure_minimal," heure/semaine")

    ##7.Pourcentage riches travaillant peu

    min_workers = df[df['hours-per-week'] == heure_minimal]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 2)

    ##8.Quel pays a le pourcentage le plus élevé de personnes gagnant plus de 50 000 $ et quel est ce pourcentage ?
    total_salaire_pays=round(df.groupby('native-country')['salary'].apply(lambda x:(x==">50K").mean()*100),2)
    #pourcentage_pays=round(total_salaire_pays*100,2)
    pays=total_salaire_pays.idxmax()
    pourcent=total_salaire_pays.max()
    print(f"le pays ayant le plud de personnes gagnant plus de 50000:{pays}\npourcentage de ce pays:{pourcent}\n")

    ##9.Identifiez la profession la plus populaire pour ceux qui gagnent > 50 000 $ en Inde.
    stat_profession=df[(df['native-country']=="India")&(df['salary']==">50K")]['occupation'].value_counts()
    profession_populaire=stat_profession.idxmax()
    print(f"La profession la plus populaire est:{profession_populaire}")

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {heure_minimal} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", pays)
        print(f"Highest percentage of rich people in country: {pourcent}%")
        print("Top occupations in India:", profession_populaire)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': heure_minimal,
        'rich_percentage': rich_percentage,
        'highest_earning_country': pays,
        'highest_earning_country_percentage': pourcent,
        'top_IN_occupation': profession_populaire
    }





results = calculate_demographic_data()

    
    
    




  