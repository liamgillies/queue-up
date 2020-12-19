import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import { AppRoutingModule } from './app-routing.module';
import { CreateProfileComponent } from './create-profile/create-profile.component';
import { ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { QueueComponent } from './queue/queue.component';


@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    CreateProfileComponent,
    QueueComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    MatCardModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  exports: [

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
