from matplotlib import pyplot as plt
import os
import cv2
import time



class searcher:

    def __init__(self, match_value=0.71, template_name="", directory="Diretorio de Busca", methods=['cv2.TM_CCOEFF_NORMED'], print_similar=False):
        self.directory = directory        
        self.template_name = template_name
        self.template_path = "{}/{}".format(directory, template_name)
        self.match_value = match_value
        self.methods = methods
        self.matches = []
        self.print_similar = print_similar
    
    def run(self):
        start = time.time()
        if self.template_name == "":
            raise Exception("O arquivo a ser usado como busca deve ser inserido")
        else:
            self.call_searcher()
            self.matches.sort(key=lambda x: x[2], reverse=True)
            for m in self.matches[25:]:
                print(m)
        
        print("Finalizado")
        end = time.time()
        print("O tempo de execução foi de: {}".format(str(end - start)))

    def call_searcher(self):
        if self.template_path.endswith(".jpg"):
            self.tatual = "{}-Imagem".format(self.template_name)
            template = cv2.imread(self.template_path, 0)
            self.search_template_in_directory(template)
        elif self.template_path.endswith(".mp4"):
            cap = cv2.VideoCapture(self.template_path)
            i = 0
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    i +=1
                    self.tatual = "{}-AFrame{}".format(self.template_name, i)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    img = gray.copy()
                    self.search_template_in_directory(img)
                else:
                    break

    def search_template_in_directory(self, template):
        for meth in self.methods:
            method = eval(meth)
            for filename in os.listdir(self.directory):
                if filename.endswith(".mp4"):
                    cap = cv2.VideoCapture('{}/{}'.format(self.directory, filename))
                    j = 0
                    while (cap.isOpened()):
                        ret, frame = cap.read()
                        if ret == True:
                            j += 1
                            self.catual = "{}-CFrame{}".format(filename, j)
                            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            img = gray.copy()
                            self.calc_search_match(img, template, method, meth)
                        else:
                            break

                elif filename.endswith(".jpg"):
                    self.catual = "{}-CImagem".format(filename)
                    img = cv2.imread('{}/{}'.format(self.directory, filename), 0)
                    img2 = img.copy()
                    self.calc_search_match(img, template, method, meth)               

    def calc_search_match(self, img, template, method, meth):
        # Aplicando o template Matching
        res = cv2.matchTemplate(img,template,method)
        #Recupera a similaridade entre o template e o conteúdo da Imagem de busca
        min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
        texto = 'Similaridade com {0} entre Imagens é {1}%'.format(meth,round(similaridade*100,2))

        if similaridade > self.match_value:
            self.matches.append((self.tatual, self.catual, similaridade))
            if self.print_similar:
                self.plt_print(template, img, texto)

    def plt_print(self, template, img, texto):
        plt.subplot(121), plt.imshow(template, cmap='gray')
        plt.title('Template'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Imagem.Frame de Busca'), plt.xticks([]), plt.yticks([])
        plt.suptitle(texto)
        plt.show()


if __name__ == "__main__":
    s = searcher(template_name="serie_face_4.jpg")
    s.run()