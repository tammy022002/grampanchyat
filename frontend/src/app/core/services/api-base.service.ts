import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BaseResponse } from '../models/base-response';

@Injectable({
  providedIn: 'root'
})
export class ApiBaseService {
  private http = inject(HttpClient);
  private baseUrl = 'http://localhost:8000/api/v1';

  get<T>(endpoint: string, params?: any): Observable<BaseResponse<T>> {
    let httpParams = new HttpParams();
    if (params) {
      Object.keys(params).forEach(key => {
        if (params[key] !== null && params[key] !== undefined) {
          httpParams = httpParams.set(key, params[key]);
        }
      });
    }
    return this.http.get<BaseResponse<T>>(`${this.baseUrl}${endpoint}`, { params: httpParams });
  }

  post<T>(endpoint: string, body: any): Observable<BaseResponse<T>> {
    return this.http.post<BaseResponse<T>>(`${this.baseUrl}${endpoint}`, body);
  }

  put<T>(endpoint: string, body: any): Observable<BaseResponse<T>> {
    return this.http.put<BaseResponse<T>>(`${this.baseUrl}${endpoint}`, body);
  }

  delete<T>(endpoint: string): Observable<BaseResponse<T>> {
    return this.http.delete<BaseResponse<T>>(`${this.baseUrl}${endpoint}`);
  }
}
