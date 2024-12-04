import requests

def generate_text(input_text, adapter_id, adapter_source, max_new_tokens, temperature, authorization_token):
    """
    Sends a POST request to the Predibase API to generate text.

    Args:
        input_text (str): The input prompt for the model.
        adapter_id (str): The adapter ID to use.
        adapter_source (str): The adapter source.
        max_new_tokens (int): Maximum number of new tokens to generate.
        temperature (float): Sampling temperature.
        authorization_token (str): Bearer token for authentication.

    Returns:
        dict: The response from the API as a dictionary.
    """
    url = "https://serving.app.predibase.com/a2f486/deployments/v2/llms/llama-3-1-8b-instruct/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {authorization_token}",
    }
    payload = {
        "inputs": input_text,
        "parameters": {
            "adapter_id": adapter_id,
            "adapter_source": adapter_source,
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
        },
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":
    input_text = '''
    Request: Provide a detailed analysis of the following study for academic purposes.

        Article: 
Citation: Garrido-Cardenas, J.A.;
González-Cerón, L.; García-Maroto,
F.; Cebrián-Carmona, J.;
Manzano-Agugliaro, F.; Mesa-Valle,
C.M. Analysis of Fifty Years of Severe
Malaria Worldwide Research.
Pathogens 2023, 12, 373. https://
doi.org/10.3390/pathogens12030373

Academic Editor: Julio
Gallego-Delgado

Received: 30 January 2023
Revised: 21 February 2023
Accepted: 23 February 2023
Published: 24 February 2023

Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

pathogens

Article

Analysis of Fifty Years of Severe Malaria Worldwide Research

Jose A. Garrido-Cardenas 1,* , Lilia Gonz á lez-Cer ó n 2 , Federico Garc í a-Maroto 3, Jos é Cebri á n-Carmona 1 ,
Francisco Manzano-Agugliaro 4 and Concepci ó n M. Mesa-Valle 1

1 Department of Biology and Geology, University of Almeria, 04120 Almeria, Spain
2 Regional Center for Public Health Research, National Institute of Public Health,

Tapachula 30700, Chiapas, Mexico
3 Department of Chemistry and Physics, University of Almeria, 04120 Almeria, Spain
4 Department of Engineering, University of Almeria, 04120 Almeria, Spain

* Correspondence: jcardena@ual.es

Abstract: This study analyzed ﬁfty years of severe malaria research worldwide. Malaria is a parasitic
disease that continues to have a signiﬁcant impact on global health, particularly in sub-Saharan Africa.
Severe malaria, a severe and often fatal form of the disease, is a major public health concern. The study
used different bibliometric indicators such as the number of publications, citations, authorship, and
keywords to analyze the research trends, patterns, and progress made in the ﬁeld of severe malaria.
The study covers the period from 1974 to 2021 and includes articles from Scopus. The results of the
study indicated that there has been a steady increase in the number of publications on severe malaria
over the past ﬁfty years, with a particular increase in the last decade. The study also showed that most
of the publications are from USA and Europe, while the disease occurs in Africa, South-East Asia, and
the Americas. The study also identiﬁed the most frequent keywords used in the publications, and the
most inﬂuential journals and authors in the ﬁeld. In conclusion, this bibliometric study provides a
comprehensive overview of the research trends and patterns in the ﬁeld of severe malaria over the
past ﬁfty years and highlights the areas that need more attention and research efforts.

Keywords: plasmodium falciparum; malaria pathogenesis; malaria treatment; severe malaria
symptoms; malaria epidemiology

1. Introduction
Malaria is one of the deadliest infectious diseases in the world. It is caused, in humans,
by six species of parasitic protozoa of the genus Plasmodium: P. falciparum (responsible
for most deaths, and mainly present in Africa), P. vivax (the species with the largest geo-
graphical distribution outside Africa), P. knowlesi, P. malariae, P. ovale wallikeri, and P. ovale
curtisi [1]. Most reported cases of severe malaria are caused by P. falciparum, although the
burden of P. vivax and P. knowlesi cannot be neglected [2].
The term severe malaria was ﬁrst described in 1985 at the ﬁrst WHO meeting convened
by the Malaria Action Programme of the World Health Organization, and since then, this
complication of the disease has been the focus of global research [3].
Mortality due to complications of severe malaria depends on multiple factors, such as
the medical circumstances surrounding the patient, the treatment received, and the course
of the infection itself. Patient frailty due to factors not directly associated with malaria, such
as age, co-infection with viruses or bacteria, or a weak immune system, can lead to death,
regardless of the infecting parasite [4, 5]. Severe malaria usually has a mortality rate of more
than 5%, which is high compared to uncomplicated malaria cases, where the mortality rate
is as low as 0.1% [6]. Severe malaria is generally evenly distributed across all population
groups in areas of low malaria transmission, but the situation is different in areas of high
transmission, where the risk is higher among non-immune people such as young children
and visitors from non-endemic areas [7, 8].

Pathogens 2023, 12, 373. https://doi.org/10.3390/pathogens12030373 https://www.mdpi.com/journal/pathogens

Pathogens 2023, 12, 373 2 of 10

Although severe malaria is often deﬁned in epidemiological or research terms, the
most practical way of delineating it is usually associated with the clinical features or the
vital organ dysfunction it causes. Thus, the most prevalent clinical features in patients with
severe malaria are: generalized weakness that may lead to the prostration of the patient;
continued failure of consciousness and other neurological abnormalities; profound anemia,
with the presence of hemoglobin in the urine (also due to acute kidney injury); respiratory
problems, with increased frequency and frequent pauses; circulatory collapse or shock,
with systolic blood pressure < 80 mmHg in adults and <50 mmHg in children; hemorrhages;
pulmonary edema; convulsions; and clinical jaundice plus evidence of other vital organ
dysfunction [9]. These clinical manifestations may occur in isolation or, more frequently, in
combination in the same patient [10]. In most cases, these pathological events are associated
with the sequestration of erythrocytes containing metabolically active parasites, which
causes alterations in the coagulation and cytopreservation pathways [11].
According to WHO estimates, the majority of malaria cases do not develop into
severe malaria. This only occurs in less than 1% of diagnosed cases (619,000 deaths out
of 247 million reported cases, according to the most recent data) [12]. Of the hundreds
of thousands of deaths each year, two-thirds involve children under ﬁve years. Children
hospitalized with anemia resulting from an episode of severe malaria have a high mortality
rate in the months following admission [13].
Even in children who survive the disease, the consequences are often dire. In about
10% of cases, a neurological deﬁcit occurs causing seizures after recovery, in addition to
a clinical picture of stroke. It is suggested that this is because a large vascular territory of
the brain area is involved in the development of the disease. In addition, other mental and
behavioral problems often appear with increasing frequency [14, 15].
It is, therefore, necessary to continue working to improve early diagnosis and treatment
in cases of severe malaria, as well as to prevent the after-effects of the disease. To this end,
it is essential to know how far we have come in the last ﬁve decades and where we are now.

2. Materials and Methods
The methodology for this bibliometric study on the analysis of ﬁfty years of severe
malaria worldwide research will involve the following steps:
Data collection: The study used a comprehensive search strategy to collect data from
the Scopus database. The choice of the Scopus database was based on the idea that it has
the most articles, journals, books, and publishers indexed [16]. Scopus is the database
developed by Elsevier, with publications from 1788 to the present day, and its use offered a
sample size that is statistically sufﬁciently representative of what is to be shown. For this
reason, Scopus is the most widely used database in bibliometric analyses of areas as
different as medicine [17], social sciences [18], or agriculture [19]. In this case, the search
was limited to articles published between 1974 and 2021, in English and other languages,
such as Spanish, French, Russian, Chinese, etc. The search terms included keywords related
to severe malaria such as “severe malaria”, “malaria pathogenesis”, “malaria treatment”
and “malaria epidemiology”.
Data screening: The collected data were screened to ensure that they met the inclusion
criteria, which included articles on severe malaria and its management. Articles that did
not meet the inclusion criteria were excluded from the study.
Data analysis: The data was analyzed using bibliometric indicators such as the number
of publications, citations, authorship patterns, and keywords. The data were analyzed
using the software VOSviewer (version 1.6.18).
Results and discussion: The results are presented in tables and ﬁgures to show the
research trends and patterns in the ﬁeld of severe malaria over the past ﬁfty years. The re-
sults were also discussed in the context of the existing literature on causes or complications
leading to severe malaria.

Pathogens 2023, 12, 373 3 of 10

Conclusion: The study highlighted the areas that need more attention and research
efforts in the ﬁeld of severe malaria and the implications of the ﬁndings for future research
in this ﬁeld.

3. Results
3.1. Global Evolution Trend of Scientiﬁc Output
The search returned 3794 documents. Figure 1 shows the global evolution trend of the
number of documents on severe malaria since the ﬁrst article was published, from 1974
until 2021, which is the year with all updated data. As can be observed in Figure 1, these
ﬁve decades were divided into three stages. The ﬁrst of these runs from 1974 to 1986. In this
period, 25 articles were published, with no trend of growth over time. The real take-off in
publications on severe malaria occurred from 1987 onwards, and a linear growth trend can
be observed until 2009, which was only altered in 2001 when there was a relative low that
broke the trend. The third stage covers the period from 2009 onwards, and it is in this stage
that the highest number of articles published per year in the entire chronology studied was
recorded. Speciﬁcally, this last stage showed an average of 184 articles published each year.

Pathogens 2023, 12, x FOR PEER REVIEW 3 of 10

results were also discussed in the context of the existing literature on causes or complica-
tions leading to severe malaria.
Conclusion: The study highlighted the areas that need more attention and research
efforts in the field of severe malaria and the implications of the findings for future research
in this field.

3. Results
3.1. Global Evolution Trend of Scientific Output
The search returned 3794 documents. Figure 1 shows the global evolution trend of
the number of documents on severe malaria since the first article was published, from
1974 until 2021, which is the year with all updated data. As can be observed in Figure 1,
these five decades were divided into three stages. The first of these runs from 1974 to 1986.
In this period, 25 articles were published, with no trend of growth over time. The real
take-off in publications on severe malaria occurred from 1987 onwards, and a linear
growth trend can be observed until 2009, which was only altered in 2001 when there was
a relative low that broke the trend. The third stage covers the period from 2009 onwards,
and it is in this stage that the highest number of articles published per year in the entire
chronology studied was recorded. Specifically, this last stage showed an average of 184
articles published each year.

Figure 1. Trend in the number of publications per year on severe malaria over the last fifty years.

Since the late 1980s, severe malaria has received increasing attention from the inter-
national scientific community (Figure 1). From then until now, the disease has been very
present in the scientific literature. In two of the years (2012 and 2014), relative peaks were
reached with more than 200 articles published.

3.2. Publication Distribution by Authors, Institutions, and Countries
The 12 most important authors in severe malaria with at least fifty publications each
are shown in Table 1. The percentage of publications on severe malaria ranged from 8.8%
(Nicholas P.J. Day, of the Mahidol Oxford Tropical Medicine Research Unit, in Bangkok,
Thailand) to 30.2% (Robert Opika Opoka, of Makerere University, in Kampala, Uganda).

Figure 1. Trend in the number of publications per year on severe malaria over the last ﬁfty years.

Since the late 1980s, severe malaria has received increasing attention from the inter-
national scientiﬁc community (Figure 1). From then until now, the disease has been very
present in the scientiﬁc literature. In two of the years (2012 and 2014), relative peaks were
reached with more than 200 articles published.

3.2. Publication Distribution by Authors, Institutions, and Countries
The 12 most important authors in severe malaria with at least ﬁfty publications each
are shown in Table 1. The percentage of publications on severe malaria ranged from 8.8%
(Nicholas P.J. Day, of the Mahidol Oxford Tropical Medicine Research Unit, in Bangkok,
Thailand) to 30.2% (Robert Opika Opoka, of Makerere University, in Kampala, Uganda).

Pathogens 2023, 12, 373 4 of 10

Table 1. Main authors highlighting severe malaria, the institutions to which they belong, and the
countries in which these institutions are located.

Author N P N% Institution Country
White, N.J. 169 1296 13.0 Mahidol University Thailand
Marsh, K. 114 520 21.9 Centre for Geographic, Medicine Research Kenya
Kremsner, P.G. 90 751 12.0 Eberhard Karls Universität, Tübingen Germany
Dondorp, A.M. 78 526 14.8 Mahidol University Thailand
Looareesuwan, S. 75 512 14.6 Hospital for Tropical Diseases Thailand
Day, N.P.J. 67 785 8.5 Mahidol Oxford Tropical, Medicine Research Unit Thailand
Anstey, N.M. 65 346 18.8 Menzies School of Health, Research Australia
Kain, K.C. 60 401 15.0 University Health Network, University of Toronto Canada
Krishna, S. 59 281 21.0 University of London United Kingdom
Newton, C.R.J.C. 56 501 11.2 Pwani University Kenya
Maitland, K. 54 201 26.9 Imperial College London United Kingdom
Opoka, R.O. 51 169 30.2 Makerere University Uganda
N: Number of severe malaria publications. P: Number of total publications.

The 12 authors belonged to institutions from 7 different countries (Thailand, Kenya,
Germany, Australia, Canada, United Kingdom, and Uganda), and above all, the researcher
Nicholas John White, from the Faculty of Tropical Medicine, in the Mahidol University
(Bangkok, Thailand), stood out with 169 publications on severe malaria. Nicholas J. White
is a British medical researcher who has devoted his research to tropical medicine, especially
malaria, in developing countries. White has established important research networks
throughout his research life and has co-written articles with more than 3000 researchers
from all over the world, some of them presented in Table 1, such as AM Dondorp or
NPJ Day.
Figure 2 shows the 10 institutions with at least 100 publications on severe malaria.
As can be noted, some of the institutions listed in Table 1 also appear in this list, but not all
of those in Figure 2 appear in Table 1. This is the case of the University of Oxford, which
appears ﬁrst in the ranking, with almost 10% of the publications on severe malaria, but
does not appear in Table 1.

Pathogens 2023, 12, x FOR PEER REVIEW 4 of 10

Table 1. Main authors highlighting severe malaria, the institutions to which they belong, and the
countries in which these institutions are located.

Author N P N% Institution Country
White, N.J. 169 1296 13.0 Mahidol University Thailand
Marsh, K. 114 520 21.9 Centre for Geographic, Medicine Research Kenya
Kremsner, P.G. 90 751 12.0 Eberhard Karls Universität, Tübingen Germany
Dondorp, A.M. 78 526 14.8 Mahidol University Thailand
Looareesuwan, S. 75 512 14.6 Hospital for Tropical Diseases Thailand

Day, N.P.J. 67 785 8.5
Mahidol Oxford Tropical, Medicine Research
Unit
Thailand

Anstey, N.M. 65 346 18.8 Menzies School of Health, Research Australia

Kain, K.C. 60 401 15.0
University Health Network, University of To-
ronto
Canada

Krishna, S. 59 281 21.0 University of London
United King-
dom
Newton, C.R.J.C. 56 501 11.2 Pwani University Kenya

Maitland, K. 54 201 26.9 Imperial College London
United King-
dom
Opoka, R.O. 51 169 30.2 Makerere University Uganda
N: Number of severe malaria publications. P: Number of total publications.

The 12 authors belonged to institutions from 7 different countries (Thailand, Kenya,
Germany, Australia, Canada, United Kingdom, and Uganda), and above all, the re-
searcher Nicholas John White, from the Faculty of Tropical Medicine, in the Mahidol Uni-
versity (Bangkok, Thailand), stood out with 169 publications on severe malaria. Nicholas
J. White is a British medical researcher who has devoted his research to tropical medicine,
especially malaria, in developing countries. White has established important research net-
works throughout his research life and has co-written articles with more than 3000 re-
searchers from all over the world, some of them presented in Table 1, such as AM Don-
dorp or NPJ Day.
Figure 2 shows the 10 institutions with at least 100 publications on severe malaria.
As can be noted, some of the institutions listed in Table 1 also appear in this list, but not
all of those in Figure 2 appear in Table 1. This is the case of the University of Oxford, which
appears first in the ranking, with almost 10% of the publications on severe malaria, but
does not appear in Table 1.

Figure 2. Top institutions whose researchers published the most articles on severe malaria.
Figure 2. Top institutions whose researchers published the most articles on severe malaria.

In Figure 3, the countries with the most publications on severe malaria are shown.
Among them, the United Kingdom and the United States stand out, with 932 and 808 arti-
cles, respectively. Following them are six countries with between 250 and 500 publications.
These are Thailand (360), France (340), Kenya (308), India (294), Australia (276), and Ger-
many (264). Finally, 13 countries are shown publishing between 100 and 250 articles.

Pathogens 2023, 12, 373 5 of 10

Pathogens 2023, 12, x FOR PEER REVIEW 5 of 10

In Figure 3, the countries with the most publications on severe malaria are shown.
Among them, the United Kingdom and the United States stand out, with 932 and 808
articles, respectively. Following them are six countries with between 250 and 500 publica-
tions. These are Thailand (360), France (340), Kenya (308), India (294), Australia (276), and
Germany (264). Finally, 13 countries are shown publishing between 100 and 250 articles.

Figure 3. World map with the countries publishing the most articles on severe malaria.

These 21 countries are also listed in Table 2. In this Table, not only the total number of
articles published in each country has been taken into account, but also the population and
GDP per capita have been considered. The total population data were obtained from
https://www.worldometers.info/world-population/population-by-country/ (accessed on 1
October 2022), while GDP per capita data, from https://www.worldometers.info/gdp/gdp-
per-capita/ (accessed on 1 October 2022). GDP (Gross Domestic Product) per capita is shown
in dollars and represents a country’s GDP divided by its total population.

Table 2. Countries publishing the most on severe malaria, in terms of the total population and rel-
ative wealth.

Country Publications (N)
Population (P)
(Mill. of Inhabitants)
N/P GDP Per Capita

United Kingdom 932 67.89 13.73 44,920
United States 808 331.00 2.44 59,928
Thailand 360 69.80 5.16 17,910
France 340 65.27 5.21 44,033
Kenya 308 53.77 5.73 3292
India 294 1410.75 0.21 7166
Australia 276 25.50 10.82 49,378
Germany 264 83.78 3.15 52,556
Switzerland 175 8.65 20.23 66,307
Uganda 173 45.74 3.78 1868
Nigeria 168 206.14 0.81 5887

Figure 3. World map with the countries publishing the most articles on severe malaria.

These 21 countries are also listed in Table 2. In this Table, not only the total number
of articles published in each country has been taken into account, but also the population
and GDP per capita have been considered. The total po

Use this format in your response:
        {{
            'intent': 'Detailed Analysis',
            'Background': '...',
            'Research Question': '...',
            'Study Method': '...',
            'Findings': '...',
            'Study Limitations': '...'
        }}

        Reply:
'''
    adapter_id = "academic_summary_finetune_llama3_adapter/5"
    adapter_source = "pbase"
    max_new_tokens = 1000
    temperature = 0.1
    authorization_token = "pb_Jw-99QJiXqGqZMWTibNOGA"

    try:
        result = generate_text(input_text, adapter_id, adapter_source, max_new_tokens, temperature, authorization_token)
        print(result['generated_text'])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
