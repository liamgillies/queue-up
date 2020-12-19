import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LandingComponent } from './landing/landing.component';
import { QueueComponent } from './queue/queue.component';
import { RouterModule, Routes } from '@angular/router';
import { CreateProfileComponent } from './create-profile/create-profile.component';
import { MessagingComponent } from './messaging/messaging.component';

const routes: Routes = [
  { path: '', component: LandingComponent },
  { path: 'create', component: CreateProfileComponent },
  { path: 'queue', component: QueueComponent },
  { path: 'message', component: MessagingComponent}
];

@NgModule({
  declarations: [],
  imports: [CommonModule, RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
