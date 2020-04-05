#GDP.py
def Gdp(coutryData):
     result={}
     for preCountry in coutryData.keys():
         gdpValue = [coutryData[preCountry][0] / 10000]
         for i in range(10):             
             gdpValue.append(gdpValue[-1] * (1 + coutryData[preCountry][1]))
             result[preCountry]=gdpValue
     for preCountry in coutryData.keys():
         print("{}:".format(preCountry))
         year=2017
         for i in  result[preCountry]:
             year=year+1
             print("{}年GDP：{}".format(year,i),end=',')
         print('\n')
         
          
def main():
      sourceGDP = {'America': [195558.74, 0.023], 'China': [131735.85, 0.069], 'Japan': [43421.6, 0.016],
                 'Germany': [35954.06, 0.022], 'English': [32322.81, 0.017], 'India': [26074.09, 0.064],
                 'Franch': [25865.68, 0.019], 'Italy': [19329.38, 0.015], 'Brazil': [17592.67, 0.01],
                 'Canda': [16823.68, 0.03]}
      Gdp(sourceGDP)
main()


import matplotlib.pyplot as plt
import random

class GDP():
    def __init__(self,sourceData):
        self.sourceData = sourceData
        self.loopNumber = 10
        #以2017年各个国家的GDP和增长率为基准，计算未来十年内的GDP变化情况
        self.result = {}
        for preCountry in self.sourceData.keys():
            gdpValue = [sourceData[preCountry][0] / 10000]
            for i in range(self.loopNumber):
                gdpValue.append(gdpValue[-1] * (1 + self.sourceData[preCountry][1]))
            self.result[preCountry] = gdpValue
        self.color = self.randomColor()

    #随机生成颜色
    def randomColor(self):
        result = []
        for i in range(self.loopNumber+4):
            color = '#'
            color += hex(random.randint(0,255))[2:4]
            color += hex(random.randint(0, 255))[2:4]
            color += hex(random.randint(0, 255))[2:4]
            color += '0'*(7-len(color))
            result.append(color)
        return result


    #使用matplotlib展示各国GDP变化情况
    def show(self):
        fig, ax = plt.subplots()  # 返回一个Figure实例fig 和一个 AxesSubplot实例ax
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        x = [[i for i in range(self.loopNumber)], [preCountry for preCountry in self.sourceData.keys()]]
        allY = []
        for i in range(self.loopNumber + 1):
            currY = []
            for preCountry in self.result.keys():
                currY.append(self.result[preCountry][i])
            allY.append(currY)

            ax.cla()  # 清除屏幕
            ax.set_xlabel('国家')  # 设置x轴label
            ax.set_ylabel('GDP总量(万亿美元)')  # 设置y轴label
            for (colorIndex, y) in zip(range(i + 1), reversed(allY)):
                ax.bar(x[0], y, color=self.color[colorIndex])
            for xT, yT in zip(x[0], allY[-1]):
                ax.text(xT - 0.3, yT + 0.3, str(round(yT, 2)), fontdict={'size': 10, 'color': 'black'})

            ax.text(8, 25, '第' + str(i + 2017) + '年', fontdict={'size': 15, 'color': 'red'}) #指定区域显示文字
            plt.ylim((0, 28))  # 设置y轴的坐标范围
            plt.xticks(x[0], x[1], rotation=60)  # 设置x轴的刻度以及刻度对应的描述
            plt.title('世界经济展望')  # 设置标题
            plt.pause(1)  # 停留1S
        plt.show()
