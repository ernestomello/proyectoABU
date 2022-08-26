import { SpinnerService } from './spinner.service';
import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';

@Injectable()
export class SpinnerInterceptor implements HttpInterceptor {

  constructor(private readonly _spinnerSvc: SpinnerService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    this._spinnerSvc.show();
    return next.handle(request).pipe(
      finalize(() => this._spinnerSvc.hide())
    );
  }
}
