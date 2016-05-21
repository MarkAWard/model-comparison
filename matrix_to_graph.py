import pickle
import json
import sys

names = {
 u'Accounting': u'Accounting',
 u'Biotech-Biomedical 01-19-16': u'Bio Engineering',
 u'Business_Dev': u'Business Development',
 u'Consulting': u'Consulting',
 u'DataScience 01-29-16': u'Data Science',
 u'EducationManagement 01-19-16': u'Education Management',
 u'Entrepreneur': u'Entrepreneurship',
 u'Frontend 02-19-16': u'Frontend Engineering',
 u'General Management 01/23/16': u'General Management',
 u'HR and Recruiting: 1/27/2016': u'HR and Recruiting',
 u'IT and Services 3-3-2016': u'Information Technology and Services',
 u'Lawyer 03/03/16': u'Law',
 u'Marketing': u'Marketing',
 u'MarketingManager 02-08-16': u'Marketing Management',
 u'Merchandiser 03/03/16': u'Merchandising',
 u'Nonprofit 03/03/16': u'Nonprofit',
 u'Operations 01/20/16': u'Operations',
 u'Product_Dev': u'Product Development',
 u'Product_Manag': u'Product Management',
 u'Project_Manag': u'Project Management',
 u'QA_Engineer 03/03/16': u'Quality Assurance Engineering',
 u'Retail_Banking 02/29/16': u'Retail Banking',
 u'STEM_osvm 3-3-2016': u'STEM Research',
 u'Sales v2 (1/5/2016)': u'Sales',
 u'Software_Development 2-21-2016': u'Software Engineering',
 u'Strategic_Planning': u'Strategic Planning',
 u'Systems_Engineering 03/03/16': u'Systems Engineering',
 u'UX_Designer 03/03/16': u'UX Design',
 u'Writer 03/08/16': u'Writing',
 u'f_CORP': u'Corporate Finance',
 u'f_HF': u'Hedge Fund',
 u'f_IB 3': u'Investment Banking',
 u'f_IM': u'Investment Management',
 u'f_PE': u'Private Equity',
 u'f_Research': u'Research Analyst',
 u'f_ST': u'Sales and Trading',
 u'f_VC': u'Venture Capital'
}


if __name__ == '__main__':
    # if len(sys.argv) != 5:
    #     print "INVALID: run script as\n\tpython matrix_to_graph.py <pickle-input> <output-json> minscale maxscale"
    if len(sys.argv) != 3:
        print "INVALID: run script as\n\tpython matrix_to_graph.py <pickle-input> <output-json>"
        sys.exit()
    else:
        _, pfile, jsonfile = sys.argv
#         _, pfile, jsonfile, newmin, newmax = sys.argv
#         newmin, newmax = float(newmin), float(newmax)
# ]
    with open(pfile, "rb") as infile:
        df = pickle.load(infile)

    # def scale(x, oldmin, oldmax, newmin, newmax):
    #     return (newmax - newmin) * (x - oldmin) / (oldmax - oldmin) + newmin

    # vals = filter(lambda v: v > 0, df.values.ravel())
    # f = partial(scale, oldmin=min(vals), oldmax=max(vals), newmin=newmin, newmax=newmax)

    models = df.columns
    total = len(models)
    nodes = []
    links = []
    for i in range(total):
        n = {
            "id": models[i], 
            "name": names[models[i]]
        }
        nodes.append(n)
        for j in range(i,total):
            l = {
                "source": models[i],
                "target": models[j],
                # "similarity": f(df.ix[models[i], models[j]])
                "similarity": df.ix[models[i], models[j]]
            }
            links.append(l)

    for i, l in enumerate(sorted(links, key=lambda d: d["similarity"], reverse=True)):
        l["similarity"] = i

    data = {
        "nodes": nodes,
        "links": links
    }
    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile, indent=2)

