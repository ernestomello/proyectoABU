import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { AuthService } from '@app/pages/auth/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  @Output() loggedAdmin = new EventEmitter<void>();

  isAdmin:boolean = true;

  constructor(private _authSvc: AuthService) { }

  ngOnInit(): void {
  }

  viewAdmin():void{
    this.loggedAdmin.emit();
  }

  onLogout():void{
    this._authSvc.logout();
  }

}
