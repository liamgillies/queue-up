import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {User} from "../_models/User";
import {Observable} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  getMatches(): Observable<User[]> {
    // right now this returns all users
    return this.http.get<User[]>(`http://localhost:5000/users/getmatches`);
  }

  getUserById(userId): Observable<User> {
    return this.http.get<User>('http://localhost:5000/users/getuser/' + String(userId));
  }

  createProfile(user: User): Observable<void>{
    return this.http.post<void>(`http://localhost:5000/create_profile`, user);
  }

}
