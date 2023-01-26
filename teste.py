7
# Importação das bibliotecas
from matplotlib import pyplot as plt
import os, cv2

#Faz a varredura do diretório imagens buscando arquivos JPG, JPEG e PNG.
diretorio = 'imagensTeste'
arquivos = os.listdir(diretorio)
# Leitura da imagem com a função imread()
imagem = cv2.imread('s1.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla

img = cv2.imread('s1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B
cv2.imshow("Imagem P&B", img)
#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)