import { CuotaInterface, RegistroPago } from './../../shared/models/cuota.interface';
import { catchError } from 'rxjs/operators';
import { environment } from '@env/environment';
import { Observable, throwError } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PersonalResponse } from '@app/shared/models/persona.interface';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  private readonly API_URL = environment.API_URL;

  constructor(private _http: HttpClient) { }

  getPersonalData (idSocio: number): Observable<PersonalResponse>{
    return this._http
    .get<PersonalResponse>(`${this.API_URL}/personas/${idSocio}`)
    .pipe(catchError(this.handleError));
  }

  // Devuelve el listado de todos los socios
  getSocios (): Observable<PersonalResponse []>{
    return this._http
    .get<PersonalResponse []>(`${this.API_URL}/personas`)
    .pipe(catchError(this.handleError));
  }

  getCuotasSocio (idSocio: number): Observable<CuotaInterface>{
    // Si el ID es cero o menor pide las cuotas de todos los socios
    console.log(idSocio);

    if (idSocio <= 0) {
      return this._http
      .get<CuotaInterface>(`${this.API_URL}/cuotas`)
      .pipe(
        catchError(this.handleError)
        );
    }
    // Si el ID es mayor que cero pide las cuotas de un socios
    return this._http
    .get<CuotaInterface>(`${this.API_URL}/socios/${idSocio}/cuota`)
    .pipe(catchError(this.handleError));
  }

  // Genera la o las cuotas de uno o mas socio
  generarCuotaSocio (id_socio: number, fecha_desde: Date, fecha_hasta: Date): Observable<Object>{
    const body = [{
      id_socio: id_socio,
      fecha_desde: fecha_desde,
      fecha_hasta: fecha_hasta,
    }];
    return this._http
    .post(`${this.API_URL}/cuotas/socio`, body)
    .pipe(catchError(this.handleError));
  }

  // Marca como pagada una cuota
  pagarCuota(registro_pago: RegistroPago): Observable<Object>{
    const id = registro_pago.id_cuota
    const body = [{
      metodo_pago: registro_pago.metodo_pago,
      referencia: registro_pago.descripcion
    }];
    return this._http
    .put(`${this.API_URL}/cuotas/${id}/pagar`, body)
    .pipe(catchError(this.handleError));
  }

  // Retorna todos los metodos de pago que hay en la base
  getMetodoPago (): Observable<Object>{
    return this._http
    .get(`${environment.API_URL}/metodospago`)
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
