import streamlit as st
import math

st.title("โปรแกรมคำนวณค่าบริการ")

# เลือกประเภทลูกค้า
customer_type = st.radio("เลือกประเภทลูกค้า:", ["บุคคลธรรมดา", "บริษัท"])

# กรอกข้อมูล
passengers = st.number_input("จำนวนผู้โดยสาร (คน)", min_value=0, value=1, step=1)
weight_kg = st.number_input("น้ำหนัก (กิโลกรัม)", min_value=0.0, value=0.0, step=100.0)

# ส่วนค้างคืน พร้อมช่องกรอกจำนวนวัน
stay_over = st.checkbox("มีการค้างคืน")
nights = 0
if stay_over:
    nights = st.number_input("จำนวนวันที่ค้างคืน (วัน)", min_value=1, value=1, step=1)

if st.button("คำนวณค่าบริการ"):
    # คำนวณค่าผู้โดยสาร
    passenger_fee = passengers * 50
    
    # คำนวณค่าธรรมเนียมขึ้น-ลง (1 ตัน = 85 บาท)
    tons = weight_kg / 1000
    if tons <= 1:
        billable_tons = 1 if tons > 0 else 0
    else:
        billable_tons = math.ceil(tons)
    lift_fee = billable_tons * 85
    
    # คำนวณค่าค้างคืนตามจำนวนวัน
    night_rate = 325 if customer_type == "บริษัท" else 162.50
    night_fee = (night_rate * nights) if stay_over else 0
            
    total_fee = passenger_fee + lift_fee + night_fee
    
    # แสดงผลลัพธ์แบบแจงรายละเอียดสำหรับนักบิน
    st.success("คำนวณและสรุปรายละเอียดสำเร็จ!")
    
    st.markdown("### 📋 ใบแจงรายละเอียดค่าบริการ (สำหรับนักบิน/ตรวจสอบ)")
    st.markdown(f"- **ประเภทลูกค้า:** {customer_type}")
    st.markdown(f"- **จำนวนผู้โดยสาร:** {passengers} คน (เรท 50 บาท/คน) = **{passenger_fee:,.2f} บาท**")
    st.markdown(f"- **น้ำหนักรวม:** {weight_kg:,.1f} กก. (คิดเป็น {billable_tons} ตัน | เรท 85 บาท/ตัน) = **{lift_fee:,.2f} บาท**")
    
    if stay_over:
        st.markdown(f"- **ค่าค้างคืน:** {nights} วัน (เรท {night_rate:,.2f} บาท/วัน) = **{night_fee:,.2f} บาท**")
    else:
        st.markdown(f"- **ค่าค้างคืน:** ไม่มี (0.00 บาท)")
        
    st.markdown("---")
    st.markdown(f"### **รวมยอดชำระทั้งสิ้น: {total_fee:,.2f} บาท**")