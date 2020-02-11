import web # pip installl web.py

urls = (
    '/page0', 'application.controllers.page0.Page0', #/= raiz  Hello la clase 
    '/page1','application.controllers.page1.Page1',
    '/page2','application.controllers.page2.Page2'
)
app = web.application(urls, globals())

render = web.template.render('templates/')





if __name__ == "__main__":
    web.config.debug= False
    app.run()