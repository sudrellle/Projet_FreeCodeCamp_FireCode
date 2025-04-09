import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Pandas/Dataset/StudentsPerformance.csv')
print(df.head())
print(df.columns)
niveau_parent=df.groupby('parental level of education')['parental level of education'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(14,10))
niveau_parent.plot(kind="barh")
plt.title('Repartition du niveau d\'education des parents')
plt.show()
plt.savefig('Pandas/Images/performance_students/repartition_niveau.png')
meilleurs_eleve=df.loc[df.groupby('test preparation course')['math score'].idxmax()]
print(meilleurs_eleve[['gender','math score','parental level of education']])
meilleur_eleves_niveau_etude_parrent=df[df['math score']==100]
print(meilleur_eleves_niveau_etude_parrent[['gender','parental level of education','math score','reading score','writing score','race/ethnicity','lunch','test preparation course']].sort_values(by="math score",ascending=False))
##Analyses:les eleves qui sont doué en maths sont ils forcement doués en lecture?
sns.scatterplot(x="math score",y="reading score",hue="parental level of education",style="test preparation course",data=df)
plt.axvline(df['math score'].mean(),color='r',linestyle='--')
plt.axhline(df['reading score'].mean(),color='r',linestyle='--')
plt.title('Repartition note de math vs note de lecture')
plt.show()
plt.savefig('Pandas/Images/performance_students/repertatition_math_vs_lecture.png')
df['completed']=df['test preparation course']=="completed"
note_mathematique_superieur_moyenne=df[df['math score']>df['math score'].mean()]
note_superieure_moyenne=df[(df["math score"]>df['math score'].mean()) &(df["reading score"]>df['reading score'].mean())]
note_superieure_moyenne_lecture=df[df["reading score"]>df['reading score'].mean()]
note_superieure_moyenne_lecriture=df[df["writing score"]>df['writing score'].mean()]
print(note_superieure_moyenne)
print(note_superieure_moyenne_lecture)
#porcentage_math_lecture=(note_mathematique_superieur_moyenne['reading score']==note_superieure_moyenne_lecture).mean()*100
#print("Pourcentage des eleves qui qui sont bon en math et en lecture\n",porcentage_math_lecture)
##doit on se preparer en fonction des matiere?
##est ce vrai qu'en terme de statistique il y'a plus d'eleves qui se sont preparées à l'examen de math par rapport aux autres matieres?

print(df.head(5))
prepa_math=note_mathematique_superieur_moyenne['completed'].mean()*100
prepa_reading=note_superieure_moyenne_lecture['completed'].mean()*100
prepa_ecriture=note_superieure_moyenne_lecriture['completed'].mean()*100
print('Taux de preparation parmi les performants')
print(f"Math:{prepa_math:.1f}%")
print(f"lecture:{prepa_reading:.1f}%")
print(f"ecriture:{prepa_ecriture:.1f}%")
prepa=df.groupby(['gender','test preparation course'])[['math score','reading score','writing score']].mean()
print(prepa)
sns.barplot(x=['math score','writing score','reading score'],y=[prepa_math,prepa_ecriture,prepa_reading])
plt.title('Taux de preparation parmi les performants par matiere')
plt.ylabel('% preparés')
plt.show()

##les eleves qui sont douées sur les 3 matieres
good_all=df[(df["math score"]>df['math score'].mean()) &(df["reading score"]>df['reading score'].mean())&(df["writing score"]>df['writing score'].mean())]
print(f'nombre de personne qui sont douées sur les 3 matieres:{len(good_all)}')

sns.countplot(x=note_superieure_moyenne['gender'])
plt.title('Repartion du nombre de garçon et de fille ayant eu une note de mathematique et de lecture superieure à la moyenne')
plt.show()
sns.countplot(x=note_superieure_moyenne_lecture['gender'])
plt.title('Repartion du nombre de garçon et de fille ayant eu une note de lecture superieure à la moyenne')
plt.show()
sns.countplot(x=note_superieure_moyenne_lecriture['gender'])
plt.title('Repartion du nombre de garçon et de fille ayant eu une note de l\'écriture superieure à la moyenne')
plt.show()
##Analyses des eleves qui ont eu note mathematique et lecture superieure à la moyenne
##Analyses1
print("************************************************************************************************")
print('*Analyses des eleves qui ont eu une note mathematique et lecture superieure à la moyenne********')
print("************************************************************************************************")
meilleur_group=note_superieure_moyenne.groupby('race/ethnicity')['race/ethnicity'].value_counts().sort_values(ascending=False)
print('Repartition des race ou ethnie des eleves ayant eu une note de lecture superieur à la moyenne\n',meilleur_group)
prepare_vs_none=note_superieure_moyenne.groupby('test preparation course')['test preparation course'].value_counts()
print("REpartition de ceux qui se sont preparés vs le contraine\n",prepare_vs_none)
test_male_vs_female=note_superieure_moyenne.groupby(['test preparation course','gender'])['gender'].value_counts()
print('Repartition du genre regroupé par le cours de test de preparation\n',test_male_vs_female)
male_vs_female=note_superieure_moyenne.groupby('gender')['gender'].value_counts()
print('repartition des genre\n',male_vs_female)
pourcentage=df['test preparation course'].value_counts().agg('mean')*100
#print('Pourcentage\n',pourcentage)
fig,axe=plt.subplots(ncols=2,nrows=1,figsize=(12,10),dpi=100)
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')
sns.scatterplot(x=note_superieure_moyenne['math score'],y=note_superieure_moyenne['reading score'],hue=note_superieure_moyenne['gender'],palette="tab10",ax=axe[0])
axe[0].legend(loc="best")
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')

##meilleur groupe?

sns.countplot(x=note_superieure_moyenne['race/ethnicity'],palette="viridis",ax=axe[1])
axe[1].set_title('Repartion des race des eleves ayant eu une note mathematique et de lecture superieure à la moyenne')
plt.xticks(rotation=45,ha="right")
plt.savefig('Pandas/Images/performance_students/Repartition_note_math_vs_note_superieur_moyenne.png')
plt.show()
##affiche tous les eleves qui ont eu à se preparer pour obternir une note superieur à la moyenne d'une par et d'autre part qui ne se sont pas 
##preparées mais qui ont ce meme resultat

sns.catplot(x=note_superieure_moyenne['math score'],y=note_superieure_moyenne['reading score'],col=note_superieure_moyenne['test preparation course'],kind="strip")
plt.xticks(rotation=45,ha="right")
plt.show()
##doit on se preparer en fonction des matiere?
##est ce vrai qu'en terme de statistique il y'a plus d'eleves qui se sont preparées à l'examen de math par rapport aux autres matieres?
##Repartition des niveau d'etudes des eleves qui ont eu une note de mathematique et lecture superieures à la moyenne regroupée
##d'une part des eleves qui ont eu à se preparer et d'autres part qui ne se sont pas preparer
sns.catplot(x=note_superieure_moyenne['parental level of education'],col=note_superieure_moyenne['test preparation course'],kind="count",hue=note_superieure_moyenne['parental level of education'])
plt.xticks(rotation=45,ha="right")
plt.show()
sns.catplot(x=note_superieure_moyenne['race/ethnicity'],hue=note_superieure_moyenne['parental level of education'],kind="count",col=note_superieure_moyenne['lunch'])
plt.show()
sns.catplot(x=note_superieure_moyenne['lunch'],kind="count",hue=note_superieure_moyenne['parental level of education'],col=note_superieure_moyenne['gender'])
plt.show()
sns.catplot(x=note_superieure_moyenne['gender'],kind="count",hue=note_superieure_moyenne['parental level of education'])
plt.show()
sns.catplot(x=note_superieure_moyenne['gender'],kind="count",hue=note_superieure_moyenne['parental level of education'],col=note_superieure_moyenne['test preparation course'])
plt.show()
####
print('Analyses des eleves ayant eu une note de lecture superieure à la moyenne')

##Analyses des eleves ayant eu une note de lecture superieure à la moyenne


##meilleur groupe?

sns.countplot(x=note_superieure_moyenne['race/ethnicity'],palette="viridis",ax=axe[1])
axe[1].set_title('Repartion des race des eleves ayant eu une note mathematique et de lecture superieure à la moyenne')
plt.xticks(rotation=45,ha="right")
plt.savefig('Pandas/Images/performance_students/Repartition_note_math_vs_note_superieur_moyenne.png')
plt.show()

fig,axe=plt.subplots(ncols=2,nrows=1,figsize=(12,10),dpi=100)
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')
sns.countplot(x=note_superieure_moyenne_lecture['reading score'],hue=note_superieure_moyenne_lecture['gender'],palette="tab10",ax=axe[0])
axe[0].legend(loc="best")
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')

##meilleur groupe?

sns.countplot(x=note_superieure_moyenne_lecture['race/ethnicity'],palette="viridis",ax=axe[1])
axe[1].set_title('Repartion des race des eleves ayant eu une note de lecture superieure à la moyenne')
plt.xticks(rotation=45,ha="right")
plt.savefig('Pandas/Images/performance_students/Repartition_note_lecture_superieur_moyenne.png')
plt.show()
sns.catplot(x=note_superieure_moyenne_lecture['reading score'],col=note_superieure_moyenne_lecture['test preparation course'],kind="strip")
plt.xticks(rotation=45,ha="right")
plt.show()
##doit on se preparer en fonction des matiere?
##est ce vrai qu'en terme de statistique il y'a plus d'eleves qui se sont preparées à l'examen de math par rapport aux autres matieres?
##Repartition des niveau d'etudes des eleves qui ont eu une note de  lecture superieures à la moyenne regroupée
##d'une part des eleves qui ont eu à se preparer et d'autres part qui ne se sont pas preparer
sns.catplot(x=note_superieure_moyenne_lecture['parental level of education'],col=note_superieure_moyenne_lecture['test preparation course'],kind="count",hue=note_superieure_moyenne_lecture['parental level of education'])
plt.xticks(rotation=45,ha="right")
plt.show()
sns.catplot(x=note_superieure_moyenne_lecture['race/ethnicity'],hue=note_superieure_moyenne_lecture['parental level of education'],kind="count",col=note_superieure_moyenne_lecture['lunch'])
plt.show()
sns.catplot(x=note_superieure_moyenne_lecture['lunch'],kind="count",hue=note_superieure_moyenne_lecture['parental level of education'],col=note_superieure_moyenne_lecture['gender'])
plt.show()
sns.catplot(x=note_superieure_moyenne_lecture['gender'],kind="count",hue=note_superieure_moyenne_lecture['parental level of education'])
plt.show()
sns.catplot(x=note_superieure_moyenne_lecture['gender'],kind="count",hue=note_superieure_moyenne_lecture['parental level of education'],col=note_superieure_moyenne['test preparation course'])
plt.show()

##analyses sur les notes de lecture et d'ecriture superieure à la moyenne

note_lecture_ecriture_moyenne=df[(df['reading score']>df['reading score'].mean())&(df['writing score']>df['writing score'].mean())]
fig,axe=plt.subplots(ncols=2,nrows=1,figsize=(12,10),dpi=100)
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')
sns.catplot(x=note_lecture_ecriture_moyenne['reading score'],y=note_lecture_ecriture_moyenne['writing score'],hue=note_lecture_ecriture_moyenne['gender'],palette="tab10",ax=axe[0])
axe[0].legend(loc="best")
plt.title('Repartition des eleves qui ont des notes superrieur à la moyenne')

##meilleur groupe?

sns.countplot(x=note_lecture_ecriture_moyenne['race/ethnicity'],palette="viridis",ax=axe[1])
axe[1].set_title('Repartion des race des eleves ayant eu une note de lecture superieure à la moyenne')
plt.xticks(rotation=45,ha="right")
plt.savefig('Pandas/Images/performance_students/Repartition_note_lecture_vs_ecriture_superieur_moyenne.png')
plt.show()
sns.catplot(x=note_lecture_ecriture_moyenne['reading score'],y=note_lecture_ecriture_moyenne['writing score'],col=note_lecture_ecriture_moyenne['test preparation course'],kind="strip")
plt.xticks(rotation=45,ha="right")
plt.show()
##doit on se preparer en fonction des matiere?
##est ce vrai qu'en terme de statistique il y'a plus d'eleves qui se sont preparées à l'examen de math par rapport aux autres matieres?
##Repartition des niveau d'etudes des eleves qui ont eu une note de mathematique et lecture superieures à la moyenne regroupée
##d'une part des eleves qui ont eu à se preparer et d'autres part qui ne se sont pas preparer
sns.catplot(x=note_lecture_ecriture_moyenne['parental level of education'],col=note_lecture_ecriture_moyenne['test preparation course'],kind="count",hue=note_superieure_moyenne_lecture['parental level of education'])
plt.xticks(rotation=45,ha="right")
plt.show()
sns.catplot(x=note_lecture_ecriture_moyenne['race/ethnicity'],hue=note_lecture_ecriture_moyenne['parental level of education'],kind="count",col=note_lecture_ecriture_moyenne['lunch'])
plt.show()
sns.catplot(x=note_lecture_ecriture_moyenne['lunch'],kind="count",hue=note_lecture_ecriture_moyenne['parental level of education'],col=note_lecture_ecriture_moyenne['gender'])
plt.show()
sns.catplot(x=note_lecture_ecriture_moyenne['gender'],kind="count",hue=note_lecture_ecriture_moyenne['parental level of education'])
plt.show()
sns.catplot(x=note_lecture_ecriture_moyenne['gender'],kind="count",hue=note_lecture_ecriture_moyenne['parental level of education'],col=note_lecture_ecriture_moyenne['test preparation course'])
plt.show()



