import { Component, OnInit } from '@angular/core';
import {User} from '../_models/User';
import {UserService} from '../_services/user.service';

@Component({
  selector: 'app-queue',
  templateUrl: './queue.component.html',
  styleUrls: ['./queue.component.css']
})
export class QueueComponent implements OnInit {
  matches: User[] = [];
  currentProfile = 0;

  constructor(private userService: UserService) {
  }

  ngOnInit(): void {
    this.userService.getMatches().subscribe(users => {
      this.matches = users;
    });
  }

  swipeUp(): void {

  }

  swipeDown(): void {

  }

  outOfMatches(): void {

  }
}
