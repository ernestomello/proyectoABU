import { catchError, map } from 'rxjs/operators';
import { environment } from '@env/environment';
import { Observable, throwError } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private _http: HttpClient) { }

  getPersonalData (idSocio: number){
    return this._http
    .get(`${environment.API_URL}/personas/${idSocio}`)
    .pipe(catchError(this.handleError));
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
