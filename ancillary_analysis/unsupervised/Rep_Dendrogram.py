from DeepTCR.DeepTCR import DeepTCR_U

# Instantiate training object
DTCRU = DeepTCR_U('Rep_Dendrogram',device='/gpu:2')

#Load Data from directories
DTCRU.Get_Data(directory='../../Data/Rudqvist',Load_Prev_Data=False,aggregate_by_aa=True,
               aa_column_beta=1,count_column=2,v_beta_column=7,d_beta_column=14,j_beta_column=21)

#Train VAE
DTCRU.Train_VAE(accuracy_min=0.9)
color_dict = {'Control':'limegreen','9H10':'red','RT':'darkorange','Combo':'magenta'}
DTCRU.Repertoire_Dendrogram(n_jobs=40,distance_metric='KL',
                           dendrogram_radius=0.28,repertoire_radius=0.35,Load_Prev_Data=True,gridsize=6,
                            color_dict=color_dict)