def print_heatmap(x, y, rows=3):
    hm = np.transpose(y, (0,3,1,2))

    for i in range(rows):
        j = np.random.randint(1,x.shape[0])
        plt.figure(figsize=(12, 12))
        
        # Affichage de l'image
        plt.subplot(rows,5,5*i+1)
        plt.imshow(x[j])
        plt.title('Image originale')
        
        # Affichage simultané de tous les joints
        plt.subplot(rows,5,5*i+2)
        joints = np.zeros((y.shape[1], y.shape[2]))
        for k in range(14):
            joints += hm[j][k]
        plt.imshow(joints)
        plt.title('Tous les joints')

        plt.subplot(rows, 5, 5*i+3)
        plt.imshow(hm[j][13])
        plt.title('Tête')
        
        plt.subplot(rows, 5, 5*i+4)
        plt.imshow(hm[j][7])
        plt.title('Coude droit')
        
        plt.subplot(rows, 5, 5*i+5)
        plt.imshow(hm[j][4])
        plt.title('Genou gauche')
        
        plt.show()