import { Component, OnInit } from '@angular/core';
import { Socket } from 'ngx-socket-io';
@Component({
  selector: 'app-messaging',
  templateUrl: './messaging.component.html',
  styleUrls: ['./messaging.component.css']
})
export class MessagingComponent implements OnInit {

  public messages: string[] = [];
  public person1 = {id: 293081239};
  public person2 = {id: 912387192};

  public matches = [{ign: "bobjoe"}, {ign: "poopie"}, {ign: "asdf"}, {ign: "potatomachiengun"}, {ign: "deez nuts"}]

  constructor(private socket: Socket) { }

  ngOnInit(): void {
    this.socket.on('connect', () => {
      this.socket.emit("privateMessages", "Connected")
    })

    this.socket.on('privateMessage', msg => {
      this.messages.push(msg);
    })
  }

  joinRoom(id: string) {
    this.socket.emit('join', {room: "unique room id?"});
  }

  sendPrivateMessage() {
    const text = (document.getElementById('privateMessage1') as HTMLInputElement).value;
    this.socket.emit('privateMessage', text, {room: "unique room id?"})
  }

}
