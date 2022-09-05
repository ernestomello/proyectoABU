import { CuotaInterface } from './../../shared/models/cuota.interface';
import { catchError, map } from 'rxjs/operators';
import { environment } from '@env/environment';
import { Observable, throwError } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { PersonalResponse } from '@app/shared/models/persona.interface';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private _http: HttpClient) { }

  getPersonalData (idSocio: number){
    return this._http
    .get<PersonalResponse>(`${environment.API_URL}/personas/${idSocio}`)
    .pipe(catchError(this.handleError));
  }

  getCuotas (){
    return this._http
    .get<CuotaInterface>(`${environment.API_URL}/cuotas`)
    .pipe(catchError(this.handleError));
  }

  getCuotasSocio (idSocio: number){
    return this._http
    .get<CuotaInterface>(`${environment.API_URL}/cuotas/${idSocio}`)
    .pipe(catchError(this.handleError));
  }

  generarCuotaSocio (idSocio: number){
    const body = [{
      id: "2",
      fecha_desde: "2023-01-01",
      fecha_hasta: "2023-01-01",
    }];

    return this._http
    .post<CuotaInterface>(`${environment.API_URL}/cuotas/socio`, body)
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
