import React from "react"
import { BrowserRouter, Switch, Route } from "react-router-dom"
import HomeScreen from "./features/Home/screens/HomeScreen"

const Routes = () => (
    <BrowserRouter>
        <Switch>
            <Route path="/municipalportal" component={HomeScreen}/>
        </Switch>
    </BrowserRouter>
)