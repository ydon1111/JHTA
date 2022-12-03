#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#


#점모양 변경
#점 크기 변경 
library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
    # 왼쪽에 사이드바 패널 
    # Application title
    titlePanel("Car data Test"),
    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
        selectInput(inputId = "xAxis","choose X axis",choices = c("mpg","disp","hp","drat","wt")),
        selectInput(inputId = "yAxis","choose Y axis",choices = c("wt","drat","hp","disp","mpg")),
        #점 모양을 지정할 콤보박스 추가 
        selectInput(inputId = "pch","CHOOSE SHAPE: ",choices = c("circle1"=1,"circle2"=16,"square"=22)),
        sliderInput(inputId = "cex","point size",min =0.1,max=3,value = 1)
        
        ),
    
        # 우측에 메인 패널 
        mainPanel(
           plotOutput(outputId = "mtcarsPlot")
        )
        )
    )
    

# 함수                 대응                     UI Outputs 
# renderPlot        plotOutput              그래프 출력 결과를 적용
# renderPrint       verbatimTextOutput      포맷이 포함된 텍스트 결과 적용
# renderTable       tableOutput             표 출력 결과를 적용 


# Define server logic required to draw a histogram
server <- function(input, output) {
        #콤보박스의 입력값  input$xAxis을 받아 
    #    mtcars의 삼점도를 그려 output$mtcarsPlot에 결과를 지정 
    
    output$mtcarsPlot <- renderPlot({
        title <- paste(input$xAxis," VS ",input$yAxis)
        
        
        plot(mtcars[,c(input$xAxis,input$yAxis)],
             main= title,
             pch=as.numeric(input$pch), #점모양
             cex=input$cex)             #점크기 
   
    })
}

# Run the application 
shinyApp(ui = ui, server = server)

