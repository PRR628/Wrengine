!wrengine:script

!!script {
    def myfunction() {
        if (stat.visibility(id="button") == True) {
            render.hide(id="button")
        }
    }
} !!

!export-name:script