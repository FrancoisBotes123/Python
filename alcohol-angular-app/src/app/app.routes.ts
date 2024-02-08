import { Routes } from '@angular/router';
import { PageNotFoundComponent } from '../app/components/PageNotFound/page-not-found/page-not-found.component';
import { AddDrinkComponent } from '../app/components/AddDrink/add-drink/add-drink.component';
import { AddPatronComponent } from '../app/components/AddPatron/add-patron/add-patron.component';
import { RecordConsumptionComponent } from '../app/components/RecordConsumption/record-consumption/record-consumption.component';
import { ViewSaturationComponent } from '../app/components/ViewSaturation/view-saturation/view-saturation.component';
import { ContactUsComponent } from '../app/components/ContactUs/contact-us/contact-us.component';
import { AboutUsComponent } from '../app/components/AboutUs/about-us/about-us.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
    { path: '', redirectTo: '/', pathMatch: 'full' },
    { path: 'app', component: AppComponent },
    { path: 'add-patron', component: AddPatronComponent },
    { path: 'add-drink', component: AddDrinkComponent },
    { path: 'record-consumption', component: RecordConsumptionComponent },
    { path: 'view-saturation', component: ViewSaturationComponent },
    { path: 'contact-us', component: ContactUsComponent },
    { path: 'about-us', component: AboutUsComponent },
    { path: '**', component: PageNotFoundComponent }
];
