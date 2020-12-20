import { Component, OnInit } from '@angular/core';
import { Socket } from 'ngx-socket-io';
@Component({
  selector: 'app-messaging',
  templateUrl: './messaging.component.html',
  styleUrls: ['./messaging.component.css']
})
export class MessagingComponent implements OnInit {

  public messages: string[] = [];

  //simulation since backend is unfinished
  public user = {id: 293081239};
  public room;
  public matches = [{ign: "bobjoe", id: 132413}, {ign: "poopie", id: 123123}, {ign: "asdf", id: 828378873}, {ign: "potatomachiengun", id: 8293787}, {ign: "deez nuts", id: 123123676}]

  constructor(private socket: Socket) { }

  ngOnInit(): void {
    this.socket.on('connect', () => {
      this.socket.emit("privateMessages", "Connected")
    })

    this.socket.on('privateMessage', msg => {
      this.messages.push(msg);
      console.log(this.messages)
    })
  }

  joinRoom(id: string) {
    this.socket.emit('leave', {room: this.room});
    this.room = this.user.id + id;
    this.messages = []
    console.log(this.room)
    this.socket.emit('join', {room: this.room});
  }

  sendPrivateMessage() {
    const text = (document.getElementById('privateMessage1') as HTMLInputElement).value;
    this.socket.emit('privateMessage', text, {room: this.room})
  }

}
