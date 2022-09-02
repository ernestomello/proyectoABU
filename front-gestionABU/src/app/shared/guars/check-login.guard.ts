import { AuthService } from './../../pages/auth/auth.service';
import { Injectable } from '@angular/core';
import { CanActivate} from '@angular/router';
import { Observable } from 'rxjs';
import { map, take } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class CheckLoginGuard implements CanActivate {

  constructor(private _authSvc: AuthService) {};
  canActivate(): Observable<boolean> {
    return this._authSvc.isLogged.pipe(
      take(1),
      map((isLogged: boolean) => isLogged)
    );
  }
}
