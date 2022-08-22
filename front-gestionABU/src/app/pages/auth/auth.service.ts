import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { JwtHelperService } from "@auth0/angular-jwt";

import { environment } from '@env/environment';

import { Socio, SocioResponse } from '@shared/models/socio.interface';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  readonly jwtHelper = new JwtHelperService();

  private loggeIn = new BehaviorSubject<boolean>(false);

  constructor(private _http: HttpClient) {
    this.checkToken();
   }

   get isLogged(): Observable<boolean>{
    return this.loggeIn.asObservable();
   }

  login(authData:Socio): Observable<SocioResponse | void>{
    return this._http
    .post<SocioResponse>(`${environment.API_URL}/socio/login`, authData)
    .pipe(
      map((res:SocioResponse) => {
        this.saveToken(res.token);
        this.loggeIn.next(true);
        return res;
      }),
      catchError((err)=> this.handleError(err))
    );
  }

  logout():void{
    sessionStorage.removeItem('token');
        this.loggeIn.next(false);
  }

  private checkToken():void {
    const socioToken = sessionStorage.getItem('token');
    const isExpired = this.jwtHelper.isTokenExpired(socioToken || undefined);  // compruebo si el token ya expiro
    isExpired ? this.logout() : this.loggeIn.next(true); // uso el operador ternario si ya expiro mando al logout()
  }

  private saveToken(token:string):void {
    sessionStorage.setItem('token', token);
  }


  // Muestro los errores que surgan
  private handleError(err:any):Observable<never> {
    let errorMessage = 'Ocurrio un error';
    if (err) {
      errorMessage = `Error: code ${err.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
  }

}
